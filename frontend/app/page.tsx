'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import SearchBar from './components/search-bar';
import Image from 'next/image'

export default function CharacterPage() {
  const [character1, setCharacter1] = useState<string>('');
  const [character2, setCharacter2] = useState<string>('');
  const [error, setError] = useState<string>('');
  const router = useRouter();

  const handleBattle = () => {
    if (character1 && character2) {
      router.push(`/battle?character1=${encodeURIComponent(character1)}&character2=${encodeURIComponent(character2)}`);
    } else {
      setError('Both characters must be selected before starting the battle.');
    }
  };

  return (
    <div className='flex flex-col items-center h-screen max-w-screen overflow-y-scroll no-scrollbar 
    bg-cover bg-center' style={{ backgroundImage: `url('/images/space.jpg')` }}>
      <h1 className='mt-10 text-[#FFFF00] custom-heading'>
        Star Wars
      </h1>
      <h2 className='text-xl mb-5 text-[#3a3a3a] custom-heading2'>Character Battle</h2>

      <div className='flex items-center justify-center'>
        <Image src={'/images/x-wing.png'} height={30} width={30} alt="" className='mr-5 mt-2'></Image>
        <button
          className="mt-3 primary-btn h-10 text-lg bg-red-700 p-3 rounded-md w-28  flex items-center justify-center hover:bg-red-600"
          onClick={handleBattle}
        >
          Battle

        </button>
        <Image src={'/images/tie-fighter.png'} height={30} width={30} alt="" className='ml-5 mt-2'></Image>

      </div>
      {error && <p className="text-red-600 mt-2 ">{error}</p>}
      <div className='flex flex-row gap-36 mt-10'>
        <SearchBar onSelect={setCharacter1} />
        <SearchBar onSelect={setCharacter2} />
      </div>
    </div>
  );
}
