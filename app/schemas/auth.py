'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-03 11:30:13
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-24 20:23:08
FilePath: /services/app/schemas/auth.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class RegisterRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr
    password: str = Field(min_length=8)
    confirm_password: str = Field(alias= "confirmPassword", min_length=8)
    # 前端给的是username，取消映射了
    # username: str = Field(alias="userName", min_length=3, max_length=20)
    username: str = Field(min_length=3, max_length=20)
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    remember: bool = False
    
class RefreshRequest(BaseModel):
    refreshToken: str

class AuthResponseData(BaseModel):
    tokenType: str = "Bearer"
    accessToken: str
    refreshToken: str | None
    expiresAt: int
