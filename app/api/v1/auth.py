'''
Author: PaulDing 1031071856@qq.com
Date: 2026-03-31 18:02:03
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-05-06 14:57:46
FilePath: /services/app/api/v1/auth.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from app.schemas.auth import RegisterRequest, AuthResponseData, LoginRequest, RefreshRequest
from app.schemas.common import ApiResponse
from app.core.response import success_response
from app.services.auth import register_user, login_user, refresh_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

@router.post("/register", response_model=ApiResponse[AuthResponseData])
def register(data: RegisterRequest, db: Session = Depends(get_db)) -> ApiResponse[AuthResponseData]:
    result = register_user(data, db)
    return success_response(data=result)

@router.post("/login", response_model=ApiResponse[AuthResponseData])
def login(data: LoginRequest, db: Session = Depends(get_db)) -> ApiResponse[AuthResponseData]:
    result = login_user(data, db)
    return success_response(data=result)

@router.post("/refresh", response_model=ApiResponse[AuthResponseData])
# refresh接口不需要数据库依赖，因为它只需要验证refresh token的有效性并生成新的access token
def refresh(data: RefreshRequest):
    result = refresh_user(data);
    return success_response(data=result)