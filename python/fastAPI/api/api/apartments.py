from fastapi import APIRouter, Depends, Header, HTTPException, Query
from uuid import uuid4
from models import ApartmentCreate, ApartmentResponse
from auth import get_current_user, rate_limiter
from users import users_db

router = APIRouter(tags=["Apartments"])

apartments_db = {}
idempotency_store = {}

@router.post("/v1/apartments", response_model=ApartmentResponse)
def create_apartment(
    apartment: ApartmentCreate,
    idempotency_key: str = Header(None),
    user=Depends(get_current_user),
    _: None = Depends(rate_limiter)
):
    if idempotency_key and idempotency_key in idempotency_store:
        return idempotency_store[idempotency_key]

    apt_id = str(uuid4())
    result = {
        "id": apt_id,
        **apartment.dict()
    }

    apartments_db[apt_id] = result

    if idempotency_key:
        idempotency_store[idempotency_key] = result

    return result

@router.get("/v1/apartments")
def list_apartments(
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    include: str = Query(None),
    _: None = Depends(rate_limiter)
):
    apartments_list = list(apartments_db.values())[offset:offset+limit]
    if include:
        fields = include.split(",")
        apartments_list = [{k: v for k, v in apt.items() if k in fields} for apt in apartments_list]
    return apartments_list

@router.put("/v1/apartments/{apt_id}", response_model=ApartmentResponse)
def update_apartment(
    apt_id: str,
    apartment: ApartmentCreate,
    user=Depends(get_current_user),
    _: None = Depends(rate_limiter)
):
    if apt_id not in apartments_db:
        raise HTTPException(status_code=404, detail="Apartment not found")

    apartments_db[apt_id].update(apartment.dict())
    return apartments_db[apt_id]

@router.get("/v2/apartments")
def list_apartments_v2(
    max_price: int | None = None,
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    include: str = Query(None),
    _: None = Depends(rate_limiter)
):
    result = list(apartments_db.values())
    if max_price is not None:
        result = [a for a in result if a["price"] <= max_price]
    result = result[offset:offset+limit]
    if include:
        fields = include.split(",")
        result = [{k: v for k, v in apt.items() if k in fields} for apt in result]
    return result

#Внутренний эндпоинт
@router.get("/internal/stats")
def internal_stats(secret_key: str = Query(...)):
    if secret_key != "INTERNAL_SECRET":
        raise HTTPException(status_code=401, detail="Unauthorized")
    total_users = len(users_db)
    total_apartments = len(apartments_db)
    avg_price = sum(a["price"] for a in apartments_db.values()) / total_apartments if total_apartments else 0
    return {
        "total_users": total_users,
        "total_apartments": total_apartments,
        "average_apartment_price": avg_price
    }
