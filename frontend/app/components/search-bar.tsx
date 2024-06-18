'use client';
import React, { useState, useEffect } from 'react';
import { Autocomplete, AutocompleteItem } from '@nextui-org/autocomplete';
import GetCharacterDetails from './character-details';
import { Character } from '../lib/types';
import { fetchAllCharacters, fetchCharacterDetails } from '../lib/api';


interface SearchBarProps {
    onSelect: (value: string) => void;
}

export default function SearchBar({ onSelect }: SearchBarProps) {
    const [characters, setCharacters] = useState<string[] | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [selectedCharName, setSelectedCharName] = useState("");
    const [characterDetails, setCharacterDetails] = useState<any | null>(null);

    const onInputChange = (value: string) => {
        setSelectedCharName(value);
        if (onSelect) {
            onSelect(value);
        }
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
            const fetchCharacterData = async () => {
                try {
                    const result = await fetchCharacterDetails(selectedCharName);
                    setCharacterDetails(result!.data!);
                    setError(null);
                } catch (error: any) {
                    setError(error.message);
                    setCharacterDetails(null);
                }
            };

            fetchCharacterData();
        }
    }, [selectedCharName]);

    return (
        <div>
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
