import SearchBar from './components/search-bar';
import BattleButton from './components/battle-button'

export default function CharacterPage() {
  return (
    <div className='h-screen flex flex-col items-center'>
      <h1 className='mt-10 text-2xl font-semibold'>Star Wars Character Battle</h1>
      <div><BattleButton /></div>
      <div className='flex flex-row gap-10 mt-10'>
        <SearchBar />
        <SearchBar />
      </div>

    </div>
  );
}


