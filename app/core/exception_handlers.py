'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-04 09:39:33
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-04 21:04:04
FilePath: /services/app/core/exception_handlers.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from typing import Union,Dict, Any, List
from app.core.exceptions import AppException


def error_response(
    *,
    code: str,
    message: str,
    status_code: int,
    details:Any = None,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={
            "success": False,
            "code": code,
            "message": message,
            "data": None,
            "details": details or {},
            },
        )

# 全局异常处理器
async def app_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    if isinstance(exc, AppException):
        return error_response(
            code=exc.code,
            message=exc.message,
            status_code=exc.status_code,
            details=exc.details,
        )
    else:
        return error_response(
            code="INTERNAL_SERVER_ERROR",
            message="服务器开小差了",
            status_code=500,
            details={},
        )

# 针对不同异常类型的处理器
async def validation_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, RequestValidationError):
        return error_response(
        code="VALIDATION_ERROR",
        message="请求参数校验失败",
        status_code=422,
        details=exc.errors(),
        )
    else:
        return error_response(
        code="INTERNAL_SERVER_ERROR",
        message="服务器开小差了",
        status_code=500,
        details={},
        )

# HTTPException 处理器请求错误等
async def http_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        return error_response(
            code="HTTP_ERROR",
            message=str(exc.detail),
            status_code=exc.status_code,
            details={},
        )
    else:
        return error_response(
            code="INTERNAL_SERVER_ERROR",
            message="服务器开小差了",
            status_code=500,
            details={},
        )


async def unhandled_exception_handler(request: Request, exc: Exception):
    # 这里可以顺手 logger.exception(exc)
    return error_response(
    code="INTERNAL_SERVER_ERROR",
    message="服务器开小差了",
    status_code=500,
    details={},
    )