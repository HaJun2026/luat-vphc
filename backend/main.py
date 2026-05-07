from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import violations

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Luật Xử Lý Vi Phạm Hành Chính API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(violations.router)

CATEGORIES = [
    {"value": "giao_thong", "label": "Giao thông đường bộ"},
    {"value": "moi_truong", "label": "Môi trường"},
    {"value": "lao_dong", "label": "Lao động"},
    {"value": "y_te", "label": "Y tế"},
    {"value": "xay_dung", "label": "Xây dựng"},
    {"value": "thuong_mai", "label": "Thương mại"},
    {"value": "phong_chay", "label": "Phòng cháy chữa cháy"},
]


@app.get("/api/categories")
def get_categories():
    return CATEGORIES


@app.get("/health")
def health():
    return {"status": "ok"}
