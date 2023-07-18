from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException
from database import SessionLocal
from routes_tags import Tags
from utils.dependencies import get_db, get_user
from utils.crud_helpers import create_todo, get_todo_by_id, delete_todo, get_public_todos_for, get_user_by_id
from schemas import TodoBase, Todo
from models import User

todo_router = APIRouter(
    prefix="/todos",
    tags=[Tags.todos],
)


@todo_router.post("/create", response_model=Todo)
async def create(
    todo_data: Annotated[TodoBase, Body()],
    current_user: User = Depends(get_user),
    db: SessionLocal = Depends(get_db)
):
    todo = create_todo(db, {**todo_data.dict(), "owner_id": current_user.id})
    return todo


@todo_router.get("/get_public", response_model=list[Todo])
async def get_public(
    current_user: User = Depends(get_user),
    db: SessionLocal = Depends(get_db),
    l: int = 10
):
    public_todos = get_public_todos_for(db, current_user.id, l)
    return public_todos


@todo_router.delete("/delete/{todo_id}")
async def delete(
    todo_id: int,
    current_user: User = Depends(get_user),
    db: SessionLocal = Depends(get_db),
) -> str:
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(400, detail="No such todo")
    
    arr_id = []
    for todo in current_user.todos:
        arr_id.append(todo.id)
    if todo_id in arr_id:
        delete_todo(db, todo)
        return "OK"
    raise HTTPException(400, detail="you can't delete this todo")
    
