# Tuina of Brain - Backend Services

认知训练应用后端 API

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
uvicorn app.main:app --reload --port 8000

# 访问 API 文档
open http://localhost:8000/docs
```

## API 端点

- `POST /api/v1/training/record` - 记录训练数据
- `GET /api/v1/training/history/{module}` - 获取训练历史
- `GET /api/v1/training/stats/{module}` - 获取统计数据
- `GET /api/v1/progress/overview` - 获取总体进度
- `GET /api/v1/export/data` - 导出数据

## 项目结构

```
services/
├── app/
│   ├── api/v1/          # API 路由
│   ├── core/            # 配置、安全
│   ├── models/          # 数据模型
│   ├── schemas/         # Pydantic 模型
│   ├── services/        # 业务逻辑
│   └── utils/           # 工具函数
├── tests/               # 测试
└── scripts/
