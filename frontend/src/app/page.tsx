"use client";

import { useState, useEffect, useCallback } from "react";
import Link from "next/link";
import { getViolations, getCategories, formatFine, Violation, Category } from "@/lib/api";

const LIMIT = 10;

export default function HomePage() {
  const [violations, setViolations] = useState<Violation[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    getCategories().then(setCategories).catch(console.error);
  }, []);

  const fetchViolations = useCallback(async () => {
    setLoading(true);
    setError(false);
    try {
      const data = await getViolations({
        q: search || undefined,
        category: category || undefined,
        page,
        limit: LIMIT,
      });
      setViolations(data.items);
      setTotal(data.total);
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  }, [search, category, page]);

  useEffect(() => {
    fetchViolations();
  }, [fetchViolations]);

  const totalPages = Math.ceil(total / LIMIT);

  const categoryLabel = (val: string) =>
    categories.find((c) => c.value === val)?.label ?? val;

  return (
    <main className="min-h-screen">
      {/* Header */}
      <div className="bg-red-700 text-white py-10 px-4">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-3xl font-bold mb-1">Tra cứu Vi phạm Hành chính</h1>
          <p className="text-red-200 text-sm">
            Cơ sở dữ liệu xử lý vi phạm hành chính Việt Nam — Luật số 15/2012/QH13 (sửa đổi 2020)
          </p>
        </div>
      </div>

      {/* Search bar */}
      <div className="bg-white shadow-sm">
        <div className="max-w-4xl mx-auto px-4 py-5">
          <input
            type="text"
            placeholder="Tìm kiếm vi phạm, điều luật, nghị định..."
            value={search}
            onChange={(e) => {
              setSearch(e.target.value);
              setPage(1);
            }}
            className="w-full border border-gray-300 rounded-lg px-4 py-3 text-base focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent"
          />

          {/* Category filter */}
          <div className="flex flex-wrap gap-2 mt-3">
            <button
              onClick={() => { setCategory(""); setPage(1); }}
              className={`px-3 py-1 rounded-full text-sm font-medium transition-colors ${
                category === ""
                  ? "bg-red-700 text-white"
                  : "bg-gray-100 text-gray-600 hover:bg-gray-200"
              }`}
            >
              Tất cả
            </button>
            {categories.map((cat) => (
              <button
                key={cat.value}
                onClick={() => { setCategory(cat.value); setPage(1); }}
                className={`px-3 py-1 rounded-full text-sm font-medium transition-colors ${
                  category === cat.value
                    ? "bg-red-700 text-white"
                    : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Results */}
      <div className="max-w-4xl mx-auto px-4 py-6">
        <p className="text-sm text-gray-500 mb-4">
          {loading ? "Đang tải..." : error ? "Lỗi kết nối server" : `Tìm thấy ${total} vi phạm`}
        </p>

        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700 text-sm mb-4">
            Không thể kết nối đến server. Vui lòng thử lại sau.
          </div>
        )}

        <div className="space-y-3">
          {violations.map((v) => (
            <Link href={`/violations/${v.id}`} key={v.id} className="block">
              <div className="bg-white rounded-lg border border-gray-200 p-5 hover:shadow-md hover:border-red-300 transition-all cursor-pointer">
                <div className="flex justify-between items-start gap-4">
                  <div className="flex-1 min-w-0">
                    <span className="text-xs font-medium text-red-700 bg-red-50 px-2 py-0.5 rounded">
                      {categoryLabel(v.category)}
                    </span>
                    <h2 className="font-semibold text-gray-900 mt-2 leading-snug">{v.title}</h2>
                    {v.legal_basis && (
                      <p className="text-xs text-gray-400 mt-1">{v.legal_basis}</p>
                    )}
                  </div>
                  <div className="text-right shrink-0">
                    <p className="text-xs text-gray-400 mb-0.5">Mức phạt</p>
                    <p className="font-bold text-red-700 text-sm">{formatFine(v.min_fine)}</p>
                    {v.max_fine > v.min_fine && (
                      <p className="text-xs text-gray-400">— {formatFine(v.max_fine)}</p>
                    )}
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>

        {/* Pagination */}
        {totalPages > 1 && (
          <div className="flex justify-center items-center gap-3 mt-8">
            <button
              onClick={() => setPage((p) => Math.max(1, p - 1))}
              disabled={page === 1}
              className="px-4 py-2 rounded-lg border border-gray-300 text-sm disabled:opacity-40 hover:bg-gray-50 transition-colors"
            >
              ← Trước
            </button>
            <span className="text-sm text-gray-600">
              Trang {page} / {totalPages}
            </span>
            <button
              onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
              disabled={page === totalPages}
              className="px-4 py-2 rounded-lg border border-gray-300 text-sm disabled:opacity-40 hover:bg-gray-50 transition-colors"
            >
              Sau →
            </button>
          </div>
        )}
      </div>

      <footer className="text-center text-xs text-gray-400 py-8">
        Dữ liệu tham khảo — không thay thế tư vấn pháp lý chính thức
      </footer>
    </main>
  );
}
