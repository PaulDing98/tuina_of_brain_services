'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-03 19:15:24
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-05-06 14:54:38
FilePath: /services/app/services/auth.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from app.schemas.auth import RegisterRequest, AuthResponseData, LoginRequest, RefreshRequest
from app.utils.password import PasswordHandler
from app.models import User, Settings
from sqlalchemy.orm import Session
from app.core.exceptions import UserAlreadyExistsException, AppException, InvalidCredentialsException, TestDevelopmentException
from app.core.security import build_auth_response, verify_token
from app.db.crud import get_one_by, save_all


def register_user(data: RegisterRequest, db: Session ) -> AuthResponseData:
    # 这里应该包含用户注册的逻辑，例如保存用户信息到数据库
    # 以及生成 JWT 令牌等
    # 判断密码和确认密码是否匹配
    if data.password != data.confirm_password:
        raise AppException(
            code="PASSWORD_NOT_MATCH",
            message="两次输入的密码不一致",
            status_code=400,
            )
    # 用email检查用户是否已经存在
    # db_user = get_one_by(db, User, email=str(data.email))
    if (db_user:= get_one_by(db, User, email=str(data.email))) is not None:
        raise UserAlreadyExistsException()
    # hash加密密码
    hashed_password = PasswordHandler.hash(data.password)
    # TODO 检查密码强度
    # if not PasswordHandler.is_strong_password(data.password):
        # raise ValueError("Password is not strong enough")
    # 创建存储用户对象
    user = User(
        email=str(data.email),
        username=data.username,
        hashed_password=hashed_password,
        )
    settings = Settings(user=user)
    save_all(db, user, settings, refresh_objects=[user, settings])
    # 模拟注册成功并返回令牌
    return build_auth_response(str(user.id))
    
def login_user(data: LoginRequest, db: Session) -> AuthResponseData:
    # 1. 根据 email 查找用户
    db_user = get_one_by(db, User, email=str(data.email))
    # 如果表里没有这个用户，抛出异常
    if not db_user:
        raise InvalidCredentialsException()
    # 2. 验证密码
    if not PasswordHandler.verify(data.password, str(db_user.hashed_password)):
        raise InvalidCredentialsException()
    # 3. 生成无refreshToken令牌
    return build_auth_response(str(db_user.id), data.remember)

# 刷新token
def refresh_user(data: RefreshRequest) -> AuthResponseData:
    # raise TestDevelopmentException()
    user_id = verify_token(data.refreshToken, token_type= "refresh")
    return build_auth_response(str(user_id))