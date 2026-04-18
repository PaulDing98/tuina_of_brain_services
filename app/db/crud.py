'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-18 21:03:53
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-18 21:20:05
FilePath: /services/app/db/crud.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from collections.abc import Sequence
from typing import Any

from sqlalchemy.orm import Session

from app.core.exceptions import DatabaseOperationException

# filter条件过滤找到row数据
def get_one_by(db: Session, model: Any, **filters: Any):
    query = db.query(model)
    for field_name, value in filters.items():
        query = query.filter(getattr(model, field_name) == value)
    return query.first()

# 保存封装
def save(db: Session, obj: Any, *, refresh: bool = True) -> Any:
    try:
        db.add(obj)
        db.commit()
        if refresh:
            db.refresh(obj)
        return obj
    except Exception as exc:
        db.rollback()
        raise DatabaseOperationException() from exc


def save_all(
    db: Session,
    *objects: Any,
    refresh_objects: Sequence[Any] | None = None,
) -> tuple[Any, ...]:
    try:
        for obj in objects:
            db.add(obj)
        db.commit()
        for obj in refresh_objects or ():
            db.refresh(obj)
        return objects
    except Exception as exc:
        db.rollback()
        raise DatabaseOperationException() from exc