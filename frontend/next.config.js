/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // Enables static exports for GitHub Pages
  basePath: '/Todo',
  assetPrefix: '/Todo/',
  images: {
    unoptimized: true,
  },
};

module.exports = nextConfig;
