'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-04 09:39:24
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-05-04 12:54:57
FilePath: /services/app/core/exceptions.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
class AppException(Exception):
    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = 400,
        details: dict | list | None = None,
        ):
            super().__init__(message)
            self.code = code
            self.message = message
            self.status_code = status_code
            self.details = details or {}


class DatabaseOperationException(AppException):
    def __init__(self):
        super().__init__(
        code="DATABASE_ERROR",
        message="数据库操作失败",
        status_code=500,
        )

class UserAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(
        code="USER_ALREADY_EXISTS",
        message="用户已存在",
        status_code=409,
        )
        
class UserDidNotExistsException(AppException):
    def __init__(self):
        super().__init__(
        code="USER_DID_NOT_EXISTS",
        message="用户不存在",
        status_code=401,
        )
        
class InvalidCredentialsException(AppException):
    def __init__(self):
        super().__init__(
        code="INVALID_CREDENTIALS",
        message="账号或密码错误",
        status_code=401,
        )
        
class TestDevelopmentException(AppException):
    def __init__(self):
        super().__init__(
        code="TESTING",
        message="测试专业",
        status_code=409,
        )
        

class ExpiredCredentialsException(AppException):
    def __init__(self):
        super().__init__(
        code="EXPIRED_CREDENTIALS",
        message="无效或过期的登录凭证",
        status_code=401,
        )

class PermissionDeniedException(AppException):
    def __init__(self):
        super().__init__(
        code="PERMISSION_DENIED",
        message="无权限访问",
        status_code=403,
        )