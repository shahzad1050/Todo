/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  basePath: '/todo',
  assetPrefix: '/todo/',
  images: {
    unoptimized: true,
  },
};

module.exports = nextConfig;
