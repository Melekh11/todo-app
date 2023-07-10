from utils.crud_helpers import get_user_by_id
from sqlalchemy.orm import Session
from fastapi import HTTPException
from hashlib import sha256
from models import User as UserModel
import os


def decode_token(db: Session, token: str) -> UserModel:
    token_data = token.split(":")
    user_id = int(token_data[0])
    token_payload = token_data[1]
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    
    payload = user.login + os.environ["SECRET_SOULT"]
    if sha256(payload.encode('utf-8')).hexdigest() == token_payload:
        return user
    raise HTTPException(status_code=401, detail="Invalid authentication credentials")
 

def encode_token(user: UserModel) -> str:
    token_data = user.login + os.environ["SECRET_SOULT"]
    token = str(user.id) + ":" + sha256(token_data.encode('utf-8')).hexdigest()
    return token
