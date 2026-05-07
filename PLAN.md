# PLAN.md — Kế hoạch triển khai

## Mục tiêu

Xây dựng web tra cứu vi phạm hành chính Việt Nam, full-stack, có URL public, tối giản nhưng đủ dùng.

## Stack quyết định

| Thành phần | Lựa chọn | Lý do |
|-----------|----------|-------|
| Frontend | Next.js 14 | App Router, TypeScript, deploy dễ |
| Backend | FastAPI (Python) | Nhanh, type-safe, OpenAPI tự sinh |
| Database | PostgreSQL | Hỗ trợ tốt trên Railway, full-text search sau này |
| Deploy | Railway | Free tier, auto-detect Python + Node, domain public |
| CSS | Tailwind CSS | Không cần design system phức tạp |

## Phases

### Phase 1 — Khởi tạo project ✅
- [x] Tạo cấu trúc monorepo `backend/` + `frontend/`
- [x] Viết README.md, CLAUDE.md, PLAN.md
- [x] Tạo `.gitignore`

### Phase 2 — Backend ✅
- [x] FastAPI app với CORS
- [x] SQLAlchemy models + PostgreSQL
- [x] API: `GET /api/violations` (search + filter + pagination)
- [x] API: `GET /api/violations/{id}`
- [x] API: `GET /api/categories`
- [x] Seed data: ~24 vi phạm thực tế từ 7 lĩnh vực
- [x] Procfile cho Railway

### Phase 3 — Frontend ✅
- [x] Next.js 14 App Router + TypeScript + Tailwind
- [x] Trang chủ: search bar + category filter + danh sách kết quả + pagination
- [x] Trang chi tiết: mức phạt, căn cứ pháp lý, phạt bổ sung, khắc phục hậu quả
- [x] API client (`src/lib/api.ts`) + `formatFine()` hiển thị VND

### Phase 4 — Deploy (TODO)
- [ ] Tạo GitHub repo: `luat-vphc`
- [ ] Push code lên GitHub
- [ ] Tạo Railway project → connect GitHub repo
- [ ] Deploy backend service + add PostgreSQL plugin
- [ ] Chạy `python seed.py` trên Railway terminal
- [ ] Deploy frontend service + set `NEXT_PUBLIC_API_URL`
- [ ] Kiểm tra URL public hoạt động

## Cải tiến tương lai (không nằm trong scope hiện tại)

- Tìm kiếm full-text với PostgreSQL `to_tsvector`
- Thêm trang admin để nhập dữ liệu
- Xuất PDF kết quả tìm kiếm
- Hỗ trợ tìm kiếm theo mức phạt (range slider)
- Thêm dữ liệu từ các nghị định mới nhất
- Chatbot AI tra cứu pháp luật (Claude API)
- PWA / mobile app

## Loạt web tiếp theo đề xuất

| # | Dự án | Mô tả |
|---|-------|-------|
| 2 | Phạt vi phạm giao thông | Chuyên sâu giao thông: ô tô, xe máy, xe tải |
| 3 | Luật lao động | Quyền lợi NLĐ, hợp đồng, BHXH |
| 4 | Thủ tục hành chính | Tra cứu hồ sơ, thời gian, cơ quan tiếp nhận |
| 5 | Văn bản pháp luật | Full-text search Luật, Nghị định, Thông tư |
| 6 | Chatbot pháp luật AI | Hỏi đáp bằng ngôn ngữ tự nhiên (Claude API) |
