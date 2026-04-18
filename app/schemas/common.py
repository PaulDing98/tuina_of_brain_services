'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-04 09:39:51
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-18 23:30:09
FilePath: /services/app/schemas/common.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    success: bool = True
    # TODO 前端拿到的是data.data ？那里多套了一层
    data: T
    message: str | None = None