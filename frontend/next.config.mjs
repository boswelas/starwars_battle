/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: false,
    images: {
        remotePatterns: [
            { hostname: "static.wikia.nocookie.net" },
            { hostname: "img.icons8.com" }
        ]
    },
    async rewrites() {
        return [
            {
                source: '/api/:path*',
                destination: 'https://starwarsbattle-production.up.railway.app/:path*' // Proxy to Flask backend
            }
        ]
    }
};

export default nextConfig;
