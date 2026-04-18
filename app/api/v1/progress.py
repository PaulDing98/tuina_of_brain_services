from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/overview")
def get_overview():
    # MVP: 返回模拟数据，后续从数据库读取
    return {
        "totalSessions": 0,
        "totalTime": 0,
        "streakDays": 0,
        "lastTrainingDate": None
    }

@router.get("/streak")
def get_streak():
    return {"currentStreak": 0, "maxStreak": 0}