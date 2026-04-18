from fastapi import APIRouter, Response
import json

router = APIRouter()

@router.get("/data")
def export_data():
    # MVP: 导出所有训练数据
    data = {"export": "training_data"}
    return Response(
        content=json.dumps(data, ensure_ascii=False, indent=2),
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=tuina-data.json"}
    )