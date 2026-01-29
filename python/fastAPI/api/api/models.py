from pydantic import BaseModel
from datetime import datetime
from typing import Optional

#Users
class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    created_at: datetime
    token: Optional[str] = None

#Apartments
class ApartmentCreate(BaseModel):
    city: str
    price: int
    rooms: int

class ApartmentResponse(BaseModel):
    id: str
    city: str
    price: int
    rooms: int
