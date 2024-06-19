import Image from 'next/image';
import { useState } from 'react';

export default function GetCharacterDetails({ characterDetails }: any) {
    const { details, image_url } = characterDetails;
    const [viewDetails, setViewDetails] = useState(false)

    const onClick = () => {
        if (viewDetails) {
            setViewDetails(false)
        } else {
            setViewDetails(true)
        }
    }

    return (
        <div className='mt-3 mb-8'>
            {image_url && (
                <div>
                    <Image src={image_url} alt="Character Image" width={200} height={200} />
                </div>
            )}
            {viewDetails ? (
                <div>
                    <button onClick={onClick} className='text-red-500'>Hide Details</button>
                    <ul>
                        {details.map((detail: any, index: number) => (
                            <li key={index}>
                                {detail.section_header && <h2>{detail.section_header}</h2>}
                                <strong>{detail.label}:</strong>
                                <div >
                                    {detail.values.map((val: any, i: any) => (
                                        <li key={i}>{val}</li>
                                    ))}
                                </div>

                            </li>
                        ))}
                    </ul></div>) : (
                <button onClick={onClick} className='text-blue-500'>View Details</button>
            )}

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
