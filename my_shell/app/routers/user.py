
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

fake_users_db = []

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    new_user = User(id=len(fake_users_db) + 1, **user.dict())
    fake_users_db.append(new_user)
    return new_user

    
@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10):
    return fake_users_db[skip: skip + limit]
