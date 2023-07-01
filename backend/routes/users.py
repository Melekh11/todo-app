# TODO: collecting cookie as user data

from fastapi import APIRouter, Depends, Body, HTTPException
from utils.dependencies import get_db
from utils.crud_helpers import create_user, get_user_by_login, create_hash, update_user_data, get_user_by_id, delete_user
from database import SessionLocal
from tags import Tags
from schemas import User as UserSchema, UserLogin, UserCreate, UserChange
from typing import Annotated

user_router = APIRouter(
    prefix="/users",
    tags=[Tags.users],
)


@user_router.post("/auth", response_model=UserSchema)
async def auth(user_data: Annotated[UserCreate, Body()], db: SessionLocal = Depends(get_db)):
    user = get_user_by_login(db, user_data.login)
    if user:
        raise HTTPException(status_code=400, detail="Login already registered")
    new_db_user = create_user(db, user_data)
    new_user = {"id": new_db_user.id, "login": new_db_user.login, "todos": new_db_user.todos}
    return new_user


@user_router.post("/login", response_model=UserSchema)
async def login(user_data: Annotated[UserLogin, Body()], db: SessionLocal = Depends(get_db)):
    user = get_user_by_login(db, user_data.login)
    if user:
        if create_hash(user_data.password) == user.hashed_password:
            return {"id": user.id, "login": user.login, "todos": user.todos}
        raise HTTPException(status_code=400, detail="Wrong password")
    raise HTTPException(status_code=400, detail="No user with that login")


@user_router.put("/change", response_model=UserSchema)
async def change_data(user_data: Annotated[UserChange, Body()], db: SessionLocal = Depends(get_db)):
    user = get_user_by_id(db, user_data.id)
    if not user:
        raise HTTPException(status_code=400, detail="No user with that login")
    new_db_user = update_user_data(db, user, user_data)
    new_user = {"id": new_db_user.id, "login": new_db_user.login, "todos": new_db_user.todos}
    return new_user


@user_router.delete("/delete/{user_id}")
async def delete(user_id: int, db: SessionLocal = Depends(get_db)) -> str:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=400, detail="No such user")
    delete_user(db, user_id)
    return "OK"
