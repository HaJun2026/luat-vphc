import Link from "next/link";
import { notFound } from "next/navigation";
import { getViolation, getCategories, formatFine } from "@/lib/api";

export default async function ViolationPage({ params }: { params: { id: string } }) {
  const id = Number(params.id);
  if (isNaN(id)) notFound();

  let violation, categories;
  try {
    [violation, categories] = await Promise.all([getViolation(id), getCategories()]);
  } catch {
    notFound();
  }

  const categoryLabel =
    categories.find((c) => c.value === violation.category)?.label ?? violation.category;

  return (
    <main className="min-h-screen">
      {/* Header */}
      <div className="bg-red-700 text-white py-8 px-4">
        <div className="max-w-3xl mx-auto">
          <Link href="/" className="text-red-300 hover:text-white text-sm mb-4 inline-block transition-colors">
            ← Quay lại danh sách
          </Link>
          <p className="text-red-300 text-sm">{categoryLabel}</p>
          <h1 className="text-2xl font-bold mt-1 leading-snug">{violation.title}</h1>
        </div>
      </div>

      <div className="max-w-3xl mx-auto px-4 py-8">
        <div className="bg-white rounded-xl border border-gray-200 overflow-hidden">
          {/* Fine banner */}
          <div className="bg-red-50 border-b border-red-100 px-6 py-5">
            <p className="text-xs font-semibold text-red-600 uppercase tracking-wide mb-2">
              Mức xử phạt tiền
            </p>
            <p className="text-3xl font-bold text-red-700">{formatFine(violation.min_fine)}</p>
            {violation.max_fine > violation.min_fine && (
              <p className="text-gray-500 text-sm mt-1">
                đến{" "}
                <span className="font-semibold text-red-600">{formatFine(violation.max_fine)}</span>
              </p>
            )}
          </div>

          {/* Details */}
          <div className="px-6 py-5 divide-y divide-gray-100">
            {violation.description && (
              <div className="py-4 first:pt-0">
                <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-wide mb-2">
                  Mô tả hành vi vi phạm
                </h3>
                <p className="text-gray-700 leading-relaxed">{violation.description}</p>
              </div>
            )}

            {violation.legal_basis && (
              <div className="py-4">
                <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-wide mb-2">
                  Căn cứ pháp lý
                </h3>
                <p className="text-gray-700">{violation.legal_basis}</p>
              </div>
            )}

            {violation.additional_penalty && (
              <div className="py-4">
                <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-wide mb-2">
                  Hình thức phạt bổ sung
                </h3>
                <p className="text-gray-700">{violation.additional_penalty}</p>
              </div>
            )}

            {violation.remedial_measure && (
              <div className="py-4">
                <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-wide mb-2">
                  Biện pháp khắc phục hậu quả
                </h3>
                <p className="text-gray-700">{violation.remedial_measure}</p>
              </div>
            )}

            <div className="py-4">
              <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-wide mb-2">
                Lĩnh vực
              </h3>
              <span className="text-sm font-medium text-red-700 bg-red-50 px-3 py-1 rounded-full">
                {categoryLabel}
              </span>
            </div>
          </div>
        </div>

        <p className="text-center text-xs text-gray-400 mt-6">
          Thông tin mang tính tham khảo — vui lòng đối chiếu văn bản pháp luật hiện hành
        </p>
      </div>
    </main>
  );
}
