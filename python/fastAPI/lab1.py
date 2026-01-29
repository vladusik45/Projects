from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from uuid import uuid4
from datetime import datetime, timedelta
import jwt

app = FastAPI(title="Apartment Purchase API", version="2.2")

# --------------------
# In-memory storage
# --------------------
users_db: Dict[str, dict] = {}  
apartments_db: Dict[str, dict] = {}
idempotency_cache: Dict[str, dict] = {}
rate_limit_store: Dict[str, list] = {}

RATE_LIMIT = 100  
RATE_PERIOD = 60  

security = HTTPBearer()

JWT_SECRET = "SECRET_KEY"
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = 60

# --------------------
# Models
# --------------------
class UserCreate(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: str
    email: str
    created_at: datetime

class UserWithToken(User):
    token: str

class ApartmentCreate(BaseModel):
    title: str
    city: str
    price: int
    rooms: int
    area: float
    description: Optional[str] = None

class Apartment(BaseModel):
    id: str
    title: str
    city: str
    price: int
    rooms: int
    area: float
    description: Optional[str]
    owner_id: str
    created_at: datetime

# --------------------
# Utilities
# --------------------
def rate_limiter(request: Request):
    client_ip = request.client.host
    now = datetime.utcnow()

    requests = rate_limit_store.get(client_ip, [])
    requests = [r for r in requests if (now - r).seconds < RATE_PERIOD]

    if len(requests) >= RATE_LIMIT:
        retry_after = RATE_PERIOD - (now - requests[0]).seconds
        raise HTTPException(
            status_code=429,
            detail="Too Many Requests",
            headers={
                "Retry-After": str(retry_after),
                "X-Limit-Remaining": "0"
            }
        )

    requests.append(now)
    rate_limit_store[client_ip] = requests


def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_id = payload.get("sub")
    if user_id not in users_db:
        raise HTTPException(status_code=401, detail="User not found")

    return users_db[user_id]

# --------------------
# Users (authentication)
# --------------------
@app.post("/api/v1/users", response_model=UserWithToken, dependencies=[Depends(rate_limiter)])
def create_user(user: UserCreate):
    user_id = str(uuid4())

    user_record = {
        "id": user_id,
        "email": user.email,
        "password": user.password,
        "created_at": datetime.utcnow()
    }

    users_db[user_id] = user_record

    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        "id": user_id,
        "email": user.email,
        "created_at": user_record["created_at"],
        "token": token
    }


@app.get("/api/v1/users", response_model=List[User], dependencies=[Depends(rate_limiter)])
def list_users(user=Depends(authenticate)):
    return [
        {"id": u["id"], "email": u["email"], "created_at": u["created_at"]}
        for u in users_db.values()
    ]


@app.delete("/api/v1/users/{user_id}", dependencies=[Depends(rate_limiter)])
def delete_user(user_id: str, user=Depends(authenticate)):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    del users_db[user_id]
    return {"status": "user deleted"}

# --------------------
# Apartments
# --------------------
@app.post("/api/v2/apartments", response_model=Apartment, dependencies=[Depends(rate_limiter)])
def create_apartment(
    apartment: ApartmentCreate,
    idempotency_key: Optional[str] = Header(None),
    user=Depends(authenticate)
):
    if idempotency_key and idempotency_key in idempotency_cache:
        return idempotency_cache[idempotency_key]

    apartment_id = str(uuid4())
    record = {
        "id": apartment_id,
        **apartment.dict(),
        "owner_id": user["id"],
        "created_at": datetime.utcnow()
    }

    apartments_db[apartment_id] = record

    if idempotency_key:
        idempotency_cache[idempotency_key] = record

    return record


@app.get("/api/v2/apartments", response_model=List[Apartment], dependencies=[Depends(rate_limiter)])
def list_apartments(
    city: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    rooms: Optional[int] = None,
    priority: Optional[str] = None
):
    results = list(apartments_db.values())

    if city:
        results = [a for a in results if a["city"] == city]
    if min_price:
        results = [a for a in results if a["price"] >= min_price]
    if max_price:
        results = [a for a in results if a["price"] <= max_price]
    if rooms:
        results = [a for a in results if a["rooms"] == rooms]
    if priority:
        results = [a for a in results if a["priority"] == priority]

    return results


@app.get("/api/v2/apartments/{apartment_id}", response_model=Apartment, dependencies=[Depends(rate_limiter)])
def get_apartment(apartment_id: str):
    if apartment_id not in apartments_db:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return apartments_db[apartment_id]


@app.delete("/api/v2/apartments/{apartment_id}", dependencies=[Depends(rate_limiter)])
def delete_apartment(apartment_id: str, user=Depends(authenticate)):
    apartment = apartments_db.get(apartment_id)
    if not apartment:
        raise HTTPException(status_code=404, detail="Apartment not found")
    if apartment["owner_id"] != user["id"]:
        raise HTTPException(status_code=403, detail="Forbidden")

    del apartments_db[apartment_id]
    return {"status": "deleted"}


@app.get("/health")
def healthcheck():
    return {"status": "ok"}
