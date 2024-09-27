'use client';
import React, { useState, useEffect } from 'react';
import { Autocomplete, AutocompleteItem } from '@nextui-org/autocomplete';
import GetCharacterDetails from './character-details';
import { fetchAllCharacters, fetchCharacterDetails, getCharImage } from '../apis/api';
import Image from 'next/image';


interface SearchBarProps {
    onSelect: (value: string) => void;
}

export default function SearchBar({ onSelect }: SearchBarProps) {
    const [characters, setCharacters] = useState<string[] | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [selectedCharName, setSelectedCharName] = useState("");
    const [characterDetails, setCharacterDetails] = useState<any | null>(null);
    const [altImage, setAltImage] = useState("")
    const [loading, setLoading] = useState(false);

    const onInputChange = (value: string) => {
        if (characters && characters.includes(value)) {
            setSelectedCharName(value);
            if (onSelect) {
                onSelect(value);
            }
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
                    setLoading(true);
                    const result = await fetchCharacterDetails(selectedCharName);
                    setLoading(false);
                    let parsedDetails;
                    if (result.data.details === 'Details unavailable') {
                        parsedDetails = result.data.details;
                    }
                    else {
                        parsedDetails = JSON.parse(result.data.details);
                    };
                    setCharacterDetails({ ...result.data, details: parsedDetails });
                    const alt = await getCharImage(selectedCharName);
                    setAltImage(alt.data)
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
        <div className='w-[16rem]'>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {characters && (
                <div>
                    <div className="flex w-full flex-wrap md:flex-nowrap gap-4 text-black ">
                        <Autocomplete
                            label="Choose a character"
                            className="max-w-xs"
                            onInputChange={onInputChange}
                        >
                            {characters.map((name) => (
                                <AutocompleteItem key={name} value={name} className="text-black ">
                                    {name}
                                </AutocompleteItem>
                            ))}
                        </Autocomplete>
                    </div>
                    {loading ? (
                        <div className='h-[18rem] flex flex-col items-center justify-center text-red-500 font-semibold animate-pulse'>
                            <h2>Loading character...</h2>
                        </div>
                    ) : (
                        characterDetails ? (
                            characterDetails.details !== 'Details unavailable' ? (
                                <div className='mt-6 flex flex-col items-center'>
                                    <GetCharacterDetails characterDetails={characterDetails} />
                                </div>
                            ) : (
                                <div className='mt-6 flex flex-col items-center'>
                                    <div className='flex flex-col items-center justify-center h-[18rem] overflow-hidden'>
                                        <div className=' flex items-center max-h-full justify-center'>
                                            <Image
                                                src={altImage}
                                                alt="Character Image"
                                                width={200}
                                                height={200}
                                                layout="intrinsic"
                                                objectFit="contain"
                                                className="custom-alt-image"
                                            />
                                        </div>
                                    </div>
                                    <p className='text-sm p-2 text-neutral-500'>Details unavailable</p>
                                </div>
                            )
                        ) : null
                    )}
                </div>
            )}
        </div>
    );
}
