# Tra cứu Vi phạm Hành chính

Web tra cứu thông tin luật xử lý vi phạm hành chính Việt Nam, bao gồm mức phạt tiền, hình thức phạt bổ sung và biện pháp khắc phục hậu quả theo từng lĩnh vực.

## Tech Stack

| Layer | Công nghệ |
|-------|-----------|
| Frontend | Next.js 14 (App Router, TypeScript, Tailwind CSS) |
| Backend | Python FastAPI |
| Database | PostgreSQL |
| Deploy | Railway (backend + DB) + Railway (frontend) |

## Tính năng

- Tìm kiếm vi phạm theo từ khóa (tên, điều luật, nghị định)
- Lọc theo lĩnh vực (giao thông, môi trường, lao động, y tế, xây dựng, thương mại, PCCC)
- Xem chi tiết: mức phạt tiền, phạt bổ sung, khắc phục hậu quả, căn cứ pháp lý
- Phân trang kết quả

## API Endpoints

```
GET /api/violations?q=&category=&page=1&limit=10   # Danh sách + tìm kiếm
GET /api/violations/{id}                            # Chi tiết vi phạm
GET /api/categories                                 # Danh sách lĩnh vực
GET /health                                         # Health check
```

## Cài đặt và chạy local

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Mac/Linux

pip install -r requirements.txt

cp .env.example .env
# Chỉnh sửa DATABASE_URL trong .env

python seed.py                  # Seed dữ liệu mẫu
uvicorn main:app --reload       # Chạy server tại http://localhost:8000
```

### Frontend

```bash
cd frontend
npm install

cp .env.example .env.local
# NEXT_PUBLIC_API_URL=http://localhost:8000

npm run dev                     # Chạy tại http://localhost:3000
```

## Deploy trên Railway

### 1. Tạo project trên Railway

- Vào [railway.app](https://railway.app) → New Project
- Kết nối GitHub repo này

### 2. Deploy Backend

- Add Service → GitHub Repo → chọn folder `backend`
- Add Plugin → PostgreSQL (Railway tự tạo DATABASE_URL)
- Variables: Railway tự inject `DATABASE_URL` và `PORT`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Sau khi deploy, chạy seed: vào terminal của service → `python seed.py`

### 3. Deploy Frontend

- Add Service → GitHub Repo → chọn folder `frontend`
- Variables: `NEXT_PUBLIC_API_URL=https://<backend-url>.railway.app`
- Start Command: `npm run build && npm start`

## Biến môi trường

### Backend
| Biến | Mô tả |
|------|-------|
| `DATABASE_URL` | PostgreSQL connection string (Railway tự inject) |
| `PORT` | Port server (Railway tự inject) |

### Frontend
| Biến | Mô tả |
|------|-------|
| `NEXT_PUBLIC_API_URL` | URL của backend service trên Railway |

## Cấu trúc project

```
luat-vphc/
├── backend/
│   ├── main.py           # FastAPI app + CORS + routes
│   ├── database.py       # SQLAlchemy engine + session
│   ├── models.py         # ORM models
│   ├── schemas.py        # Pydantic schemas
│   ├── seed.py           # Seed dữ liệu mẫu
│   ├── routers/
│   │   └── violations.py # API routes cho violations
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── app/
│       │   ├── page.tsx              # Trang chủ + tìm kiếm
│       │   └── violations/[id]/page.tsx  # Trang chi tiết
│       └── lib/
│           └── api.ts                # API client + helpers
├── README.md
├── CLAUDE.md
└── PLAN.md
```

## Dữ liệu mẫu

Bao gồm ~24 vi phạm thực tế từ các nghị định:
- Nghị định 100/2019/NĐ-CP (giao thông đường bộ)
- Nghị định 45/2022/NĐ-CP (môi trường)
- Nghị định 12/2022/NĐ-CP (lao động)
- Nghị định 117/2020/NĐ-CP (y tế)
- Nghị định 16/2022/NĐ-CP (xây dựng)
- Nghị định 98/2020/NĐ-CP (thương mại)
- Nghị định 144/2021/NĐ-CP (phòng cháy chữa cháy)

> Dữ liệu mang tính tham khảo, không thay thế tư vấn pháp lý chính thức.
