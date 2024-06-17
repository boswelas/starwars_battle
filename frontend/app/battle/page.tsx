// app/battle/page.jsx
'use client';
import { useSearchParams } from 'next/navigation';

export default function BattlePage() {
    const searchParams = useSearchParams();
    const character1 = searchParams.get('character1');
    const character2 = searchParams.get('character2');

    return (
        <div className='flex flex-col items-center min-h-screen'>
            <h1 className='mt-10 text-2xl font-semibold'>
                Battle between {character1} and {character2}
            </h1>
            {/* Add the rest of your battle page content here */}
        </div>
    );
}
