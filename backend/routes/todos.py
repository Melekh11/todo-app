from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException
from database import SessionLocal
from routes_tags import Tags
from utils.dependencies import get_db
from utils.crud_helpers import create_todo, get_todo_by_id, delete_todo, get_public_todos_for, get_user_by_id
from schemas import TodoCreate, Todo

todo_router = APIRouter(
    prefix="/todos",
    tags=[Tags.todos]
)


@todo_router.post("/create", response_model=Todo)
async def create(todo_data: Annotated[TodoCreate, Body()], db: SessionLocal = Depends(get_db)):
    todo = create_todo(db, todo_data)
    return todo


@todo_router.get("/get_public/{current_user_id}", response_model=list[Todo])
async def get_public(current_user_id: int, db: SessionLocal = Depends(get_db), l: int = 10):
    user = get_user_by_id(db, current_user_id)
    if user:
        public_todos = get_public_todos_for(db, current_user_id, l)
        return public_todos
    raise HTTPException(400, detail="No user with that id")


@todo_router.delete("/delete/{todo_id}")
async def delete(todo_id: int, db: SessionLocal = Depends(get_db)) -> str:
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(400, detail="No such todo")
    delete_todo(db, todo)
    return "OK"
