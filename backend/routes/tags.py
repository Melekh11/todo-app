# TODO: add, get all

from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException
from schemas import TagCreate, Tag
from utils.dependencies import get_db
from utils.crud_helpers import create_tag, get_tag_by_value, get_tags
from database import SessionLocal
from routes_tags import Tags as RouterTags

tag_router = APIRouter(
    prefix="/tags",
    tags=[RouterTags.tags]
)

@tag_router.post("/create", response_model=Tag)
async def create(tag_data: Annotated[TagCreate, Body()], db: SessionLocal = Depends(get_db)):
    tag = get_tag_by_value(db, tag_data.value)
    if tag:
        raise HTTPException(status_code=400, detail="Tag already registered")
    new_tag = create_tag(db, tag_data)
    return new_tag

@tag_router.get("/all", response_model=list[Tag])
async def get_all(l: int | None = None, db: SessionLocal = Depends(get_db)):
    tags = get_tags(db, l)
    return tags

