from sqlalchemy.orm import Session
from schemas import UserCreate
from models import User as UserModel
from hashlib import sha256

def create_hash(text: str) -> str:
    return sha256(text.encode('utf-8')).hexdigest()


def get_user_by_id(db: Session, id: int) -> UserModel:
    return db.query(UserModel).filter(UserModel.id == id).first()


def get_user_by_login(db: Session, login: str) -> UserModel:
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

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()

