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

@router.post("/record")
def record_training(session: TrainingSession):
    session.timestamp = datetime.now().isoformat()
    training_data.append(session.dict())
    return {"status": "success", "id": len(training_data) - 1}

@router.get("/history/{module}")
def get_history(module: str, limit: int = 50):
    filtered = [s for s in training_data if s["module"] == module]
    return filtered[-limit:]

@router.get("/stats/{module}")
def get_stats(module: str):
    filtered = [s for s in training_data if s["module"] == module]
    if not filtered:
        return {"count": 0}
    
    results = [s["result"] for s in filtered]
    return {
        "count": len(filtered),
        "latest": filtered[-1],
        "best": min(results, key=lambda x: x.get("time", float("inf")))
    }