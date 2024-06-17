"use client"
import React, { useState, useEffect } from 'react';
import { fetchAllCharacters, fetchCharacter } from './lib/api';
import { Character } from './lib/types';
import SearchBar from './components/search-bar';
import { Autocomplete, AutocompleteItem } from '@nextui-org/autocomplete';
import Image from 'next/image'
import GetCharacterDetails from './components/character-details'


export default function CharacterPage() {
  const [characters, setCharacters] = useState<string[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedCharName, setSelectedCharName] = useState("");
  const [characterDetails, setCharacterDetails] = useState<Character | null>(null);

  const onInputChange = (value: string) => {
    setSelectedCharName(value!)
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
          {characterDetails && (
            <GetCharacterDetails characterDetails={characterDetails} />
          )}
        </div>
      )}
    </div>
  );
}


