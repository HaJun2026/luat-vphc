const API_URL = typeof window === "undefined"
  ? (process.env.NEXT_PUBLIC_API_URL || "https://luat-vphc-production.up.railway.app")
  : "/proxy";

export interface Violation {
  id: number;
  title: string;
  description: string | null;
  category: string;
  min_fine: number;
  max_fine: number;
  legal_basis: string | null;
  additional_penalty: string | null;
  remedial_measure: string | null;
  created_at: string;
}

export interface ViolationListResponse {
  items: Violation[];
  total: number;
  page: number;
  limit: number;
}

export interface Category {
  value: string;
  label: string;
}

export async function getViolations(params: {
  q?: string;
  category?: string;
  page?: number;
  limit?: number;
}): Promise<ViolationListResponse> {
  const sp = new URLSearchParams();
  if (params.q) sp.set("q", params.q);
  if (params.category) sp.set("category", params.category);
  if (params.page) sp.set("page", params.page.toString());
  if (params.limit) sp.set("limit", params.limit.toString());

  const res = await fetch(`${API_URL}/api/violations?${sp}`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch violations");
  return res.json();
}

export async function getViolation(id: number): Promise<Violation> {
  const res = await fetch(`${API_URL}/api/violations/${id}`, { cache: "no-store" });
  if (!res.ok) throw new Error("Violation not found");
  return res.json();
}

export async function getCategories(): Promise<Category[]> {
  const res = await fetch(`${API_URL}/api/categories`, { next: { revalidate: 3600 } });
  if (!res.ok) throw new Error("Failed to fetch categories");
  return res.json();
}

export function formatFine(amount: number): string {
  return new Intl.NumberFormat("vi-VN", {
    style: "currency",
    currency: "VND",
  }).format(amount);
}
