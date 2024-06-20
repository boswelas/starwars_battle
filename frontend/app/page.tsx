'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import SearchBar from './components/search-bar';

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
    <div className='flex flex-col items-center min-h-screen max-w-screen overflow-y-scroll no-scrollbar '>
      <h1 className='mt-10 text-3xl font-semibold mb-5'>
        Star Wars Character Battle
      </h1>

      <div className='flex items-center justify-center'>
        <button
          className="mt-3 primary-btn h-10 text-lg bg-red-600 p-3 rounded-md font-semibold flex items-center justify-center"
          onClick={handleBattle}
        >
          Battle
        </button>
      </div>
      {error && <p className="text-red-600 mt-2 ">{error}</p>}
      <div className='flex flex-row gap-36 mt-10'>
        <SearchBar onSelect={setCharacter1} />
        <SearchBar onSelect={setCharacter2} />
      </div>
    </div>
  );
}
