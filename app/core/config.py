'''
Author: PaulDing 1031071856@qq.com
Date: 2026-03-28 18:44:51
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-15 12:13:59
FilePath: /services/app/core/config.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tuina of Brain API"
    VERSION: str = "1.0.0"
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 # 1小时
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30 # 30天
    # CORS
    CORS_ORIGINS: list = ["http://localhost:5173", "http://localhost:3000"]
    
    # Database (optional for MVP)
    DATABASE_URL: str = "sqlite:///./tuina.db"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()