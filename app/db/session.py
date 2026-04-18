'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-03 20:32:16
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-03 21:38:41
FilePath: /services/app/db/session.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
DATABASE_URL = "sqlite:///./tuina.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()