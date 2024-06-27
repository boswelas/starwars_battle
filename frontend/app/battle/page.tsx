'use client';
import { notFound, redirect, useSearchParams } from 'next/navigation';
import { useEffect, useState } from 'react';
import { battle, getCharImage, scrapeCharImage } from '../apis/api';
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
    const [isLoser, setLoser] = useState("")
    const [char1Photo, setChar1Photo] = useState<string | null>(null);
    const [char2Photo, setChar2Photo] = useState<string | null>(null);
    const [altImage1, setAltImage1] = useState("")
    const [altImage2, setAltImage2] = useState("")




    function onClick() {
        setShowReference(!showReference)
    }

    useEffect(() => {
        const fetchBattle = async () => {
            try {
                const result = await battle(character1!, character2!);
                if (!character1 || !character2) {
                    return notFound();
                }
                setBattle(result.data[1] || null);
                setBattleReference(result.data[0][0] || null);
                setError(null);
                const char1 = await scrapeCharImage(character1!);
                setChar1Photo(char1.data.image_url);
                const char2 = await scrapeCharImage(character2!);
                setChar2Photo(char2.data.image_url);
                if (result.data[0][0] && result.data[0][0].length > 0) {
                    const lastItem = result.data[0][0][result.data[0][0].length - 1];
                    setLoser(lastItem);
                }
                const alt1 = await getCharImage(character1!);
                setAltImage1(alt1.data)
                const alt2 = await getCharImage(character2!);
                setAltImage2(alt2.data)
                setLoading(false);
            }
            catch (error: any) {
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
                <div className='grid grid-cols-2 gap-32 items-center items-justify mt-6'>
                    <div className='flex flex-col items-center justify-center h-[18rem] overflow-hidden'>
                        <div className={`flex items-center max-h-full justify-center ${character1 === isLoser ? 'opacity-40 filter grayscale' : ''}`}>
                            {char1Photo ? (<Image
                                src={char1Photo!}
                                alt="Character Image"
                                width={200}
                                height={200}
                                layout="intrinsic"
                                objectFit="contain"
                                className="custom-alt-image"
                            />) : (<Image
                                src={altImage1!}
                                alt="Character Image"
                                width={200}
                                height={200}
                                layout="intrinsic"
                                objectFit="contain"
                                className="custom-alt-image"
                            />)}

                        </div>
                    </div>
                    <div className='flex flex-col items-center justify-center h-[18rem] overflow-hidden'>
                        <div className={`flex items-center max-h-full justify-center ${character2 === isLoser ? 'opacity-40 filter grayscale' : ''}`}>
                            {char2Photo ? (<Image
                                src={char2Photo!}
                                alt="Character Image"
                                width={200}
                                height={200}
                                layout="intrinsic"
                                objectFit="contain"
                                className="custom-alt-image"
                            />) : (<Image
                                src={altImage2!}
                                alt="Character Image"
                                width={200}
                                height={200}
                                layout="intrinsic"
                                objectFit="contain"
                                className="custom-alt-image"
                            />)}
                        </div>
                    </div>
                </div>
                <div className="mt-10 mb-10 w-[60%] no-scrollbar overflow-y-scroll flex flex-col items-center bg-black">
                    <ul className="list-disc list-inside">
                        {battleDetails}
                    </ul>
                </div>

            </div>
            <div className='ml-[18rem] w-[60%] mb-10'>
                {showReference ? (
                    <div className='bg-black'>
                        <button className='text-red-600 text-sm' onClick={onClick}>
                            Hide Battle Reference
                        </button>
                        <p className='text-lg text-[#FFFF00]'>These are the results from the battle calculator, which were given to ChatGPT to generate the story above.</p>
                        <ul className="list-disc list-inside">
                            {battleReference!.slice(0, -1).map((result, index) => (
                                <li key={index}>{result}</li>
                            ))}
                        </ul>
                    </div>
                ) : (<button className='text-red-600 text-sm' onClick={onClick}>
                    View Battle Reference
                </button>)}
            </div>
        </div >
    );
}


