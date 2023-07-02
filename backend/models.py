from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
import datetime

from database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  login = Column(String, index=True, unique=True)
  hashed_password = Column(String)

  todos = relationship("Todo", back_populates="owner")


class Todo(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True)
  title = Column(String)
  description = Column(String)
  date_created = Column(Date, default=datetime.date.today)
  sharable = Column(Boolean)

  tag_id = Column(Integer, ForeignKey("tags.id"))
  owner_id = Column(Integer, ForeignKey("users.id"))

  tag = relationship("Tag", back_populates="todos")
  owner = relationship("User", back_populates="todos")


class Tag(Base):
  __tablename__ = "tags"

  id = Column(Integer, primary_key=True)
  value = Column(String, unique=True)

  todos = relationship("Todo", back_populates="tag")
