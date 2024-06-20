'use client';
import { useSearchParams } from 'next/navigation';
import { useEffect, useState } from 'react';
import { battle } from '../lib/api';
import Loading from './loading';
import Link from 'next/link';
import Image from 'next/image';


export default function BattlePage() {
    const searchParams = useSearchParams();
    const character1 = searchParams.get('character1');
    const character2 = searchParams.get('character2');
    const [battleDetails, setBattle] = useState<string[] | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);


    useEffect(() => {
        const fetchBattle = async () => {
            try {
                const result = await battle(character1!, character2!);
                setBattle(result.data || null);
                setError(null);
                setLoading(false)
                console.log(battleDetails)
            } catch (error: any) {
                setError(error.message);
                setBattle(null);
            }
        };

        fetchBattle();
    }, []);

    if (loading) {
        return <Loading />
    }
    return (
        <div className='flex flex-col items-center min-h-screen '>
            <div className='mb-10'>
                <Link href={"/"}>
                    <button className="mt-5 fixed right-[5%] primary-btn h-10 bg-neutral-600 p-3 rounded-md          
            flex items-center justify-center hover:bg-neutral-500">
                        Try Another Battle <Image src={'/icons8-rebel-48.png'} alt='' height={20} width={20} className='ml-1'></Image>
                    </button>
                </Link>
            </div>
            <h1 className='mt-10 text-2xl font-semibold'>
                Battle between {character1} and {character2}
            </h1>
            <div className="mt-5 mb-10">
                <h2 className="text-lg font-semibold">Battle Results:</h2>
                <ul className="list-disc list-inside">
                    {battleDetails!.map((result, index) => (
                        <li key={index}>{result}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
}
