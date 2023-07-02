from sqlalchemy.orm import Session
from schemas import UserCreate, TodoCreate, TagCreate
from models import User as UserModel, Todo as TodoModel, Tag as TagModel
from hashlib import sha256

def create_hash(text: str) -> str:
    return sha256(text.encode('utf-8')).hexdigest()

def get_user_by_id(db: Session, id: int) -> UserModel | None:
    return db.query(UserModel).filter(UserModel.id == id).first()

def get_user_by_login(db: Session, login: str) -> UserModel | None:
    return db.query(UserModel).filter(UserModel.login == login).first()

def create_user(db: Session, user: UserCreate) -> UserModel:
    hashed_password = create_hash(user.password)
    db_user = UserModel(login=user.login, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_data(db: Session, user: UserModel, new_user: UserCreate) -> UserModel:
    user.login = new_user.login
    user.hashed_password = create_hash(new_user.password)
    db.add(user)
    db.commit()
    return user

def delete_user(db: Session, user_id: int) -> None:
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()

def create_todo(db: Session, todo_data: TodoCreate) -> TodoModel:
    db_todo = TodoModel(**todo_data.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def create_tag(db: Session, tag_data: TagCreate) -> TagModel:
    tag = TagModel(value = tag_data.value)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def get_tag_by_value(db: Session, value: str) -> TagModel | None:
    return db.query(TagModel).filter(TagModel.value==value).first()

def get_tags(db: Session, l: int | None = None) -> list[TagModel]:
    if l:
        return db.query(TagModel).limit(l).all()
    return db.query(TagModel).all()

def get_todo_by_id(db: Session, id: int) -> TodoModel | None:
    return db.query(TodoModel).filter(TodoModel.id == id).first()

def delete_todo(db: Session, todo: TodoModel) -> None:
    db.delete(todo)
    db.commit()

def get_public_todos_for(db: Session, user_id: int, l: int) -> list[TodoModel]:
    return db.query(TodoModel).filter(TodoModel.owner_id != user_id, TodoModel.sharable == True).limit(l).all()
