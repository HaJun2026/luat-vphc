/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: "/proxy/:path*",
        destination: "https://luat-vphc-production.up.railway.app/:path*",
      },
    ];
  },
};

module.exports = nextConfig;
