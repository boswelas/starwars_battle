import Image from 'next/image'
import React from 'react'
import { Character } from '../lib/types'

interface GetCharacterDetailsProps {
    characterDetails: Character;
}

export default function GetCharacterDetails({ characterDetails }: GetCharacterDetailsProps) {
    return (
        <div className='mt-3'>
            <h2>Character Details</h2>
            <p>Name: {characterDetails.name}</p>
            <p>Image: <Image src={characterDetails.image} alt={characterDetails.name} width={200}
                height={200} /></p>
            <p>Range: {characterDetails.range}</p>
            <p>Base ATK: {characterDetails.base_atk}</p>
            <p>Base DEF: {characterDetails.base_def}</p>
            <p>Max ATK: {characterDetails.max_atk}</p>
            <p>Max DEF: {characterDetails.max_def}</p>
            <p>ACC: {characterDetails.acc}</p>
            <p>EVA: {characterDetails.eva}</p>
        </div>
    )
}
