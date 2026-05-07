'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-05 08:18:06
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-24 22:47:19
FilePath: /services/app/core/security.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from datetime import datetime, timedelta, timezone

from jose import jwt, ExpiredSignatureError, JWTError
from app.core.exceptions import ExpiredCredentialsException

from app.core.config import settings
from app.schemas.auth import AuthResponseData

# 生成 JWT 令牌的函数
def _create_token(user_id: str, expires_delta: timedelta, token_type: str) -> tuple[str, int]:
    expires_at = datetime.now(timezone.utc) + expires_delta
    payload = {
        "sub": user_id,
        "type": token_type,
        "iat": int(datetime.now(timezone.utc).timestamp()),
        "exp": int(expires_at.timestamp()),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token, int(expires_at.timestamp())

# accessToken
def create_access_token(user_id: str) -> str:
    access_token, _ = _create_token(
        user_id=user_id,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        token_type="access",
    )
    return access_token

# refreshToken
def create_refresh_token(user_id: str) -> str:
    refresh_token, _ = _create_token(
        user_id=user_id,
        expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        token_type="refresh",
    )
    return refresh_token


def decode_token(token: str)-> dict:
    try: 
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    # 过期报错
    except ExpiredSignatureError:
        raise ExpiredCredentialsException()
    # 解码报错
    except JWTError:
        raise ExpiredCredentialsException()
    return payload

# 验证refreshToken
# 
def verify_token(token: str, token_type : str) -> str:
    payload = decode_token(token)
    if payload.get("type") != token_type:
        raise ExpiredCredentialsException()
    if user_id := payload.get("sub"):
        return user_id
    else: 
        raise ExpiredCredentialsException()
    

# 注册登录返回用的
def build_auth_response(user_id: str, remember: bool = True) -> AuthResponseData:
    
    access_token, expires_at = _create_token(
        user_id=user_id,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        token_type="access",
    )
    refresh_token = create_refresh_token(user_id) if remember else None
    return AuthResponseData(
        tokenType="Bearer",
        accessToken=access_token,
        refreshToken=refresh_token,
        expiresAt=expires_at,
    )