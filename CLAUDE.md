# CLAUDE.md — Hướng dẫn cho Claude Code

## Tổng quan project

Web tra cứu vi phạm hành chính Việt Nam. Monorepo với 2 service độc lập:
- `backend/` — FastAPI + PostgreSQL, deploy trên Railway
- `frontend/` — Next.js 14 App Router, deploy trên Railway

## Kiến trúc

### Backend (`backend/`)
- `main.py` — khởi tạo FastAPI, CORS, mount routes, tạo tables
- `database.py` — SQLAlchemy engine, session factory, `get_db()` dependency
- `models.py` — model `Violation` với các cột: title, description, category, min_fine, max_fine, legal_basis, additional_penalty, remedial_measure
- `schemas.py` — Pydantic schemas cho request/response validation
- `routers/violations.py` — `GET /api/violations` (list + search) và `GET /api/violations/{id}`
- `seed.py` — script chạy một lần để insert dữ liệu mẫu

### Frontend (`frontend/`)
- `src/app/page.tsx` — client component, search + filter + pagination
- `src/app/violations/[id]/page.tsx` — server component, render chi tiết
- `src/lib/api.ts` — tất cả fetch calls + helper `formatFine()` (VND)

## Conventions

- Backend: Python 3.11, type hints, không dùng `async def` cho DB queries (sync SQLAlchemy)
- Frontend: TypeScript strict, Tailwind CSS, không có state management library
- Màu chủ đạo: `red-700` (màu cờ đỏ — phù hợp chủ đề pháp luật Việt Nam)
- Không dùng CSS modules, không dùng styled-components

## Thêm dữ liệu mới

Chỉnh sửa mảng `VIOLATIONS` trong `backend/seed.py`, mỗi entry gồm:
```python
{
    "title": str,           # Tên hành vi vi phạm
    "description": str,     # Mô tả chi tiết
    "category": str,        # Một trong: giao_thong, moi_truong, lao_dong, y_te, xay_dung, thuong_mai, phong_chay
    "min_fine": int,        # Mức phạt tối thiểu (VND)
    "max_fine": int,        # Mức phạt tối đa (VND)
    "legal_basis": str,     # Nghị định, điều luật áp dụng
    "additional_penalty": str | None,  # Hình thức phạt bổ sung
    "remedial_measure": str | None,    # Biện pháp khắc phục
}
```

## Thêm lĩnh vực mới

1. Thêm vào list `CATEGORIES` trong `backend/main.py`
2. Thêm vi phạm tương ứng trong `backend/seed.py`
3. Frontend tự động hiển thị category mới (fetch từ `/api/categories`)

## Môi trường

Backend đọc `DATABASE_URL` từ env — Railway tự inject. `postgres://` được convert sang `postgresql://` trong `database.py`.

Frontend đọc `NEXT_PUBLIC_API_URL` — phải set trong Railway Variables khi deploy.

## Lệnh thường dùng

```bash
# Backend
uvicorn main:app --reload          # Dev server
python seed.py                     # Seed data (chỉ chạy 1 lần)

# Frontend
npm run dev                        # Dev server
npm run build && npm start         # Production
```
