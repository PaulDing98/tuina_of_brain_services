'''
Author: PaulDing 1031071856@qq.com
Date: 2026-03-31 18:02:03
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-05-07 11:17:33
FilePath: /services/app/api/v1/settings.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from app.schemas.settings import SettingsResponseData, UpdateSettingsRequest
from app.schemas.common import ApiResponse
from app.core.response import success_response
from app.deps.auth import require_auth
from app.core.exceptions import TestDevelopmentException
from app.services.settings import get_settings, edit_settings
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

# 获取设置信息
@router.get("/me", response_model=ApiResponse[SettingsResponseData])
def me(current_user=(Depends(require_auth)), db: Session = Depends(get_db)) -> ApiResponse[SettingsResponseData]:
    result = get_settings(current_user, db)
    return success_response(data=result)

@router.patch("/me", response_model=ApiResponse[SettingsResponseData])
def edit_me_settings(data: UpdateSettingsRequest, current_user=(Depends(require_auth)), db: Session = Depends(get_db)) -> ApiResponse[SettingsResponseData]:
    raise TestDevelopmentException()
    result = edit_settings(data, current_user, db)
    return success_response(data=result)