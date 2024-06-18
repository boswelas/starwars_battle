import React from 'react';
import Image from 'next/image';

export default function GetCharacterDetails({ characterDetails }: any) {
    const { details, image_url } = characterDetails;

    return (
        <div className='mt-3'>
            <h2>Character Details</h2>
            {image_url && (
                <div>
                    <Image src={image_url} alt="Character Image" width={200} height={200} />
                </div>
            )}
            <ul>
                {details.map((detail: any, index: number) => (
                    <li key={index}>
                        <strong>{detail.label}: </strong>{detail.value}
                    </li>
                ))}
            </ul>
        </div>
    );
}







// export default function GetCharacterDetails({ characterDetails }: any) {
//     console.log(characterDetails)
//     return (
//         <div className='mt-3'>
//             <h2>Character Details</h2>
//             {characterDetails}
//             {/* <p>Name: {characterDetails.name}</p>
//             <p>Image: <Image src={characterDetails.image} alt={characterDetails.name} width={200}
//                 height={200} /></p>
//             <p>Range: {characterDetails.range}</p>
//             <p>Base ATK: {characterDetails.base_atk}</p>
//             <p>Base DEF: {characterDetails.base_def}</p>
//             <p>Max ATK: {characterDetails.max_atk}</p>
//             <p>Max DEF: {characterDetails.max_def}</p>
//             <p>ACC: {characterDetails.acc}</p>
//             <p>EVA: {characterDetails.eva}</p> */}
//         </div>
//     )
// }
