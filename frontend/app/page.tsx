"use client"
import React, { useState, useEffect } from 'react';
import { fetchAllCharacters, fetchCharacter } from './lib/api';
import { Character } from './lib/types';
import SearchBar from './components/search-bar';
import { Autocomplete, AutocompleteItem } from '@nextui-org/autocomplete';


export default function CharacterPage() {
  const [characters, setCharacters] = useState<string[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedCharName, setSelectedCharName] = useState("");
  const [characterDetails, setCharacterDetails] = useState<Character | null>(null);

  const onSelectionChange: (value: string | null) => void = (newValue) => {
    setSelectedCharName(newValue!);
  };

  const onInputChange = (value: string) => {
    setSelectedCharName(value!)
  };


  const handleInputChange = (value: string) => {
    setSelectedCharName(value);
  };

  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        const result = await fetchAllCharacters();
        setCharacters(result || null);
        setError(null);
      } catch (error: any) {
        setError(error.message);
        setCharacters(null);
      }
    };

    fetchCharacters();
  }, []);

  useEffect(() => {
    if (selectedCharName) {
      console.log("char is ", selectedCharName)
      const fetchCharacterData = async () => {
        try {
          const result = await fetchCharacter(selectedCharName);
          setCharacterDetails(result!.data!);
          console.log(characterDetails)
          setError(null);
        } catch (error: any) {
          setError(error.message);
          setCharacterDetails(null);
          console.log("set char deets null")
        }
      };

      fetchCharacterData();
    }
  }, [selectedCharName]);


  return (
    <div className='h-screen'>
      <h1>Fetch Character Data</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {characters && (
        <div>
          <div className="flex w-full flex-wrap md:flex-nowrap gap-4 text-black">
            <Autocomplete
              label="Choose a character"
              className="max-w-xs"
              onInputChange={onInputChange}
            >
              {characters.map((name) => (
                <AutocompleteItem key={name} value={name} className="text-black">
                  {name}
                </AutocompleteItem>
              ))}
            </Autocomplete>
          </div>
          {/* <SearchBar names={characters} onChange={handleInputChange} /> */}
          {characterDetails && (
            <div>
              <h2>Character Details</h2>
              <p>Name: {characterDetails.name}</p>
              <p>Image: <img src={characterDetails.image} alt={characterDetails.name} /></p>
              <p>Range: {characterDetails.range}</p>
              <p>Base ATK: {characterDetails.base_atk}</p>
              <p>Base DEF: {characterDetails.base_def}</p>
              <p>Max ATK: {characterDetails.max_atk}</p>
              <p>Max DEF: {characterDetails.max_def}</p>
              <p>ACC: {characterDetails.acc}</p>
              <p>EVA: {characterDetails.eva}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
function setSelectedCharName(charName: string) {
  throw new Error('Function not implemented.');
}

