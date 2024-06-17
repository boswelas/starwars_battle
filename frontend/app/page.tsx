
// export default function Home() {
//   return (
//     <div>
//       <div className="flex flex-col items-center pt-10">
//         <h1>Star Wars Battle</h1>
//       </div>
//       <div className="flex items-center justify-center mt-20">
//         <form className="flex">
//           <input type="text" placeholder="Search Character" className="mr-2"></input>
//         </form>
//         <form className="flex">
//           <input type="text" placeholder="Search Character" className="mr-2"></input>
//         </form>
//       </div>
//     </div>
//   );

// }
"use client"
import { useState } from 'react';
import { getCharacter } from './lib/api';
import { Character } from './lib/types';

const CharacterPage: React.FC = () => {
  const [charName, setCharName] = useState<string>('');
  const [character, setCharacter] = useState<Character | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleFetchCharacter = async () => {
    const result = await getCharacter(charName);
    if (result.error) {
      setError(result.error);
      setCharacter(null);
    } else {
      setError(null);
      setCharacter(result.data || null);
    }
  };

  return (
    <div >
      <h1>Fetch Character Data</h1>
      <input
        type="text"
        value={charName}
        onChange={(e) => setCharName(e.target.value)}
        placeholder="Enter character name"
        className=' text-black'
      />
      <button onClick={handleFetchCharacter}>Fetch Character</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {character && (
        <div>
          <h2>Character Data:</h2>
          <img src={character.image} alt={character.name} />
          <pre>{JSON.stringify(character, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default CharacterPage;
