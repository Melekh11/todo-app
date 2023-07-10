from utils.helpers import encode_token, decode_token
from fastapi import APIRouter, Depends, Body, HTTPException
from utils.dependencies import get_db, get_user, ProxyUser
from utils.crud_helpers import create_user, get_user_by_login, create_hash, update_user_data, delete_user
from database import SessionLocal
from routes_tags import Tags
from schemas import User as UserSchema, UserLogin, UserCreate, UserChange, TokenResponse
from typing import Annotated
from models import User

user_router = APIRouter(
    prefix="/users",
    tags=[Tags.users],
)


@user_router.post("/auth", response_model=TokenResponse)
async def auth(
    user_data: Annotated[UserCreate, Body()],
    db: SessionLocal = Depends(get_db)
):
    user = get_user_by_login(db, user_data.login)
    if user:
        raise HTTPException(status_code=400, detail="Login already registered")
    new_db_user = create_user(db, user_data)
    token = encode_token(new_db_user)
    token = {"access_token": token, "token_type": "bearer"}
    return token


@user_router.post("/login", response_model=TokenResponse)
async def login(
    user_data: Annotated[UserLogin, Body()],
    db: SessionLocal = Depends(get_db)
):
    user = get_user_by_login(db, user_data.login)
    if user:
        if create_hash(user_data.password) == user.hashed_password:
            token = encode_token(user)
            return {"access_token": token, "token_type": "bearer"}
        raise HTTPException(status_code=400, detail="Wrong password")
    raise HTTPException(status_code=400, detail="No user with that login")


@user_router.put("/change", response_model=TokenResponse)
async def change_data(
    user_data: Annotated[UserChange, Body()],
    db: SessionLocal = Depends(get_db),
    current_user: User = Depends(get_user)
):
    new_db_user = update_user_data(db, current_user, user_data)
    token = encode_token(new_db_user)
    return {"access_token": token, "token_type": "bearer"}


@user_router.delete("/delete")
async def delete(
    db: SessionLocal = Depends(get_db),
    current_user: User = Depends(get_user)
) -> str:
    delete_user(db, current_user.id)
    return "OK"

@user_router.get("/me", response_model=UserSchema)
async def me(current_user: User = Depends(get_user)):
    return {
        "id": current_user.id,
        "login": current_user.login,
        "todos": current_user.todos
    }
