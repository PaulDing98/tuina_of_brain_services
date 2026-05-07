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

## 依赖管理

项目现在使用 `pip-tools` 管理依赖：

- `requirements.in`：运行时直接依赖
- `requirements-dev.in`：开发依赖，在 `requirements.in` 基础上追加
- `requirements.txt`：锁定后的运行时依赖，部署环境使用
- `requirements-dev.txt`：锁定后的开发依赖

常用命令：

```bash
# 安装运行时依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -r requirements-dev.txt

# 新增运行时依赖后，重新生成锁文件
pip-compile requirements.in

# 新增开发依赖后，重新生成开发锁文件
pip-compile requirements-dev.in -o requirements-dev.txt

# 按锁文件同步当前环境（可选）
pip-sync requirements-dev.txt
```

推荐流程：

1. 把新依赖写进 `requirements.in` 或 `requirements-dev.in`
2. 运行 `pip-compile`
3. 提交 `.in` 和生成后的 `.txt`

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
