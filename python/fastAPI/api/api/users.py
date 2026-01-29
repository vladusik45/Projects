from fastapi import APIRouter, Depends, Header, Query
from uuid import uuid4
from datetime import datetime
from typing import List
from models import UserCreate, UserResponse
from auth import create_token, get_current_user, rate_limiter

router = APIRouter(tags=["Users"])

users_db = {}
idempotency_store = {}

@router.post("/v1/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    idempotency_key: str = Header(None),
    _: None = Depends(rate_limiter)
):
    if idempotency_key and idempotency_key in idempotency_store:
        return idempotency_store[idempotency_key]

    user_id = str(uuid4())
    token = create_token(user_id)

    result = {
        "id": user_id,
        "email": user.email,
        "created_at": datetime.utcnow(),
        "token": token
    }

    users_db[user_id] = result

    if idempotency_key:
        idempotency_store[idempotency_key] = result

    return result

@router.get("/v1/users", response_model=List[UserResponse])
def list_users(
    current_user=Depends(get_current_user),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    _: None = Depends(rate_limiter)
):
    users_list = list(users_db.values())
    return users_list[offset:offset+limit]

@router.delete("/v1/users/{user_id}")
def delete_user(
    user_id: str,
    current_user=Depends(get_current_user),
    _: None = Depends(rate_limiter)
):
    users_db.pop(user_id, None)
    return {"status": "deleted"}
