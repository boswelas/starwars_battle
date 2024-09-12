export default function Loading() {
    return (
        <div className="text-3xl flex flex-col items-center justify-center h-screen w-screen bg-cover bg-center" style={{
            backgroundImage: `url('/images/space.jpg')`
        }} >
            <h1 className="animate-pulse font-semibold text-[#FFFF00] custom-heading2 lowercase">Loading battle...</h1>
        </div>
    );
}
