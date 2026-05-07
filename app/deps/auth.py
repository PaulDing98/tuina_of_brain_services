'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-19 01:58:20
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-20 00:24:04
FilePath: /services/app/deps/auth.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from sqlalchemy.orm import Session
from app.core.exceptions import ExpiredCredentialsException
from app.models import User
from app.core.security import verify_token
from app.core.exceptions import UserDidNotExistsException
from fastapi import Header, Depends
from app.db.session import get_db
def token_to_user_id(authorization: str | None = Header(None))-> str:
    # 查到非Bearer Token报错
    if not authorization:
        raise ExpiredCredentialsException()
    if not authorization.startswith("Bearer "):
        raise ExpiredCredentialsException()
    return verify_token(token=authorization.split(" ")[1], token_type="access")


def require_auth(credentials: str = Depends(token_to_user_id), db: Session = Depends(get_db)) -> User:
        # 根据 user_id 查找用户
    if db_user := db.query(User).filter(User.id == credentials).first():
        return db_user
    else:
        raise UserDidNotExistsException()