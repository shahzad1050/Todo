/** @type {import('next').NextConfig} */
const nextConfig = {
  // Remove static export for Vercel deployment
  images: {
    unoptimized: true,
  },
  // Enable API routes for backend integration
  experimental: {
    serverComponentsExternalPackages: ['sqlmodel', 'fastapi'],
  },
};

module.exports = nextConfig;
