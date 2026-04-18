'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-03 20:31:51
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-18 20:11:08
FilePath: /services/app/models/user.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.settings import Settings

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    settings: Mapped["Settings"] = relationship(
        "Settings",
        back_populates="user",
        uselist=False,
    )