from utils.helpers import decode_token
from database import SessionLocal
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


def get_user(token: Annotated[str, Depends(oauth2_scheme)], db: SessionLocal = Depends(get_db)):
    user = decode_token(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user
