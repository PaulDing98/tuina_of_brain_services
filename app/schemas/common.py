'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-04 09:39:51
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-05-04 12:32:02
FilePath: /services/app/schemas/common.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    data: T | None = None
    message: str | None = None
    code: str = "OK"
    details: dict | list | None = None