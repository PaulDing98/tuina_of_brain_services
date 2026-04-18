'''
Author: PaulDing 1031071856@qq.com
Date: 2026-03-31 18:02:03
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-18 19:34:17
FilePath: /services/app/api/v1/auth.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from app.schemas.auth import RegisterRequest, AuthResponseData, LoginRequest, RefreshRequest
from app.schemas.common import ApiResponse
from app.services.auth import register_user, login_user, refresh_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

@router.post("/register", response_model=ApiResponse[AuthResponseData])
def register(data: RegisterRequest, db: Session = Depends(get_db)) -> ApiResponse[AuthResponseData]:
    print("Register endpoint called", data)
    result = register_user(data, db)
    return ApiResponse(
        success=True,
        data=result,
    )
    
@router.post("/login", response_model=ApiResponse[AuthResponseData])
def login(data: LoginRequest, db: Session = Depends(get_db)) -> ApiResponse[AuthResponseData]:
    print("Login endpoint called", data)
    result = login_user(data, db)
    return ApiResponse(success=True,
        data=result,)

@router.post("/refresh", response_model=ApiResponse[AuthResponseData])
def refresh(data: RefreshRequest):
    result = refresh_user(data);
    return ApiResponse(success=True,
        data=result
    )