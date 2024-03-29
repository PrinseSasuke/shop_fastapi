from typing import List
from app.models.user import User, UserIn
from app.repositories.users import UserRepository
from fastapi import APIRouter, Depends, HTTPException, status, Request
from .depends import get_user_repository, get_current_user
from app.templates_jinja import templates
router = APIRouter()
#POST user
@router.post("/", response_model=User)
async def create(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)
#GET user
@router.get("/", response_model=List[User])
async def read_users(users: UserRepository = Depends(get_user_repository),
                     limit: int = 100,
                     skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)
#PUT user
@router.put("/{id}", response_model=User)
async def update_user(
    id: int,
    user: UserIn,
    users: UserRepository = Depends(get_user_repository),
    current_user: User = Depends(get_current_user)):
    old_user = await users.get_by_id(id=id)
    if old_user is None  or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id=id, u=user)
