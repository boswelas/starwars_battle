'use client';
import { useSearchParams } from 'next/navigation';
import { useEffect, useState } from 'react';
import { battle, battle_calc } from '../lib/api';
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
    const [showReference, setShowReference] = useState(false);
    const [battleReference, setBattleReference] = useState<string[] | null>(null);

    function onClick() {
        setShowReference(!showReference)
    }

    useEffect(() => {
        const fetchBattle = async () => {
            try {
                const result = await battle(character1!, character2!);
                setBattle(result.data[1] || null);
                setBattleReference(result.data[0][0] || null);
                setError(null);
                setLoading(false)
                console.log("battle ref: ", battleReference)
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
        <div className='h-screen overflow-y-scroll no-scrollbar bg-cover bg-center' style={{ backgroundImage: `url('/images/space.jpg')` }}>
            <div className='flex flex-col items-center' >
                <div className='mb-10'>
                    <Link href={"/"}>
                        <button className="mt-5 fixed right-[5%] primary-btn h-10 bg-neutral-700 p-3 rounded-md          
            flex items-center justify-center hover:bg-neutral-600">
                            Try Another Battle <Image src={'/images/icons8-rebel-48.png'} alt='' height={20} width={20} className='ml-1'></Image>
                        </button>
                    </Link>
                </div>
                <div className='flex flex-col items-center text-center text-wrap text-4xl font-semibold text-[#FFFF00] '>
                    <h1 className='mt-16 custom-heading2'>
                        Battle between
                    </h1>
                    <h1 className='custom-heading2 lowercase'>{character1} and {character2}</h1>
                </div>
                <div className="mt-10 mb-10 w-[60%] no-scrollbar overflow-y-scroll flex flex-col items-center">
                    <ul className="list-disc list-inside">
                        {battleDetails}
                    </ul>
                </div>

            </div>
            <div className='ml-[18rem] w-[60%] mb-10'>
                <button className='text-red-600 font-semibold' onClick={onClick}>
                    View Battle Reference
                </button>
                {showReference && (

                    <div className=''>
                        <p className=' font-semibold'>Here are the results from the battle calculator, which were given to ChatGPT to generate the story above.</p>
                        <ul className="list-disc list-inside">
                            {battleReference!.map((result, index) => (
                                <li key={index}>{result}</li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        </div>
    );
}


