import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Tra cứu Vi phạm Hành chính",
  description: "Tra cứu thông tin luật xử lý vi phạm hành chính Việt Nam",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi">
      <body className="bg-gray-50 text-gray-900">{children}</body>
    </html>
  );
}
