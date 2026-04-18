'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-03 20:31:51
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-18 20:10:50
FilePath: /services/app/models/settings.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from sqlalchemy import Integer, DateTime,ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

from datetime import datetime
from app.db.session import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.user import User

class Settings(Base):
    __tablename__ = "settings"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    schulte_highlight_on_correct:Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    schulte_border_color_value:Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    schulte_font_color_value:Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    schulte_penalty_time:Mapped[int] = mapped_column(Integer, nullable=False, default=2500)

    sequence_sequence_length:Mapped[int] = mapped_column(Integer, nullable=False, default=5)
    sequence_display_time:Mapped[int] = mapped_column(Integer, nullable=False, default=800)
    sequence_interval_time:Mapped[int] = mapped_column(Integer, nullable=False, default=400)

    created_at:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    updated_at:Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )

    user: Mapped["User"] = relationship("User", back_populates="settings")