'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-19 01:58:20
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-05-04 11:36:49
FilePath: /services/app/api/v1/training.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter()

class TrainingSession(BaseModel):
    module: str
    result: dict
    duration: int
    config: dict
    timestamp: Optional[str] = None

# 内存存储（MVP 阶段）
training_data = []

# @router.post("/record")
# def record_training(session: TrainingSession):
#     session.timestamp = datetime.now().isoformat()
#     training_data.append(session.dict())
#     return {"status": "success", "id": len(training_data) - 1}

# @router.get("/history/{module}")
# def get_history(module: str, limit: int = 50):
#     filtered = [s for s in training_data if s["module"] == module]
#     return filtered[-limit:]

# @router.get("/stats/{module}")
# def get_stats(module: str):
#     filtered = [s for s in training_data if s["module"] == module]
#     if not filtered:
#         return {"count": 0}
    
#     results = [s["result"] for s in filtered]
#     return {
#         "count": len(filtered),
#         "latest": filtered[-1],
#         "best": min(results, key=lambda x: x.get("time", float("inf")))
#     }