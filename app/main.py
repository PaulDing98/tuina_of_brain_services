'''
Author: PaulDing 1031071856@qq.com
Date: 2026-03-28 18:44:51
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-04 09:59:46
FilePath: /services/app/main.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from app.api.v1 import training, progress, export, auth, settings
from app.db.session import engine, Base
import app.models # 确保 User 模型被导入注册
from app.core.exceptions import AppException
from app.core.exception_handlers import app_exception_handler, validation_exception_handler, http_exception_handler,unhandled_exception_handler


Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Tuina of Brain API",
    description="认知训练应用后端服务",
    version="1.0.0"
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 路由
app.include_router(training.router, prefix="/api/v1/training", tags=["training"])
app.include_router(progress.router, prefix="/api/v1/progress", tags=["progress"])
app.include_router(export.router, prefix="/api/v1/export", tags=["export"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(settings.router, prefix="/api/v1/settings", tags=["settings"])


# 全局异常处理

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)
@app.get("/")
def root():
    return {
        "message": "Tuina of Brain API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)