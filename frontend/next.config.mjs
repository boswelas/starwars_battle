/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: false,
    images: {
        remotePatterns: [
            { hostname: "static.wikia.nocookie.net" },
            { hostname: "img.icons8.com" }
        ]
    },
};

export default nextConfig;
