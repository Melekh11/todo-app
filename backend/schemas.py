from pydantic import BaseModel
from datetime import date


class TagBase(BaseModel):
  value: str


class TagCreate(TagBase):
  pass


class Tag(TagBase):
  id: int

  class Config:
      orm_mode = True


class TodoBase(BaseModel):
  title: str
  description: str
  date_created: date
  sharable: bool
  tag_id: int
  

class TodoCreate(TodoBase):
  pass


class Todo(TodoBase):
  id: int
  tag: Tag

  class Config:
        orm_mode = True


class UserBase(BaseModel):
  login: str

class UserCreate(UserBase):
  password: str

class UserLogin(UserCreate):
  pass

class UserChange(UserCreate):
  id: int

class User(UserBase):
  id: int
  todos: list[Todo] = []