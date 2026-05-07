'''
Author: PaulDing 1031071856@qq.com
Date: 2026-03-28 18:44:51
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-05-07 16:11:21
FilePath: /services/app/core/config.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache
import os
from pathlib import Path
from dotenv import load_dotenv
# 获取项目根目录（假设 config.py 在项目根目录）
BASE_DIR = Path(__file__).resolve().parent.parent
# 指定 .env 文件路径
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)


cors_origins = os.getenv("CORS_ORIGINS")

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tuina of Brain API"
    VERSION: str = "1.0.0"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 # 1小时
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7 # 7天
    SECRET_KEY: Optional[str] = os.getenv("SECRET_KEY")
    # CORS
    CORS_ORIGINS: Optional[list] = cors_origins.split(",") if cors_origins else []
    # Database (optional for MVP)
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
print("Loaded settings:", settings.dict())
print(settings.SECRET_KEY)
print(settings.CORS_ORIGINS)
print(settings.DATABASE_URL)
