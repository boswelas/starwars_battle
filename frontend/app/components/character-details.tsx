import Image from 'next/image';
import { useState } from 'react';

interface CharacterDetails {
    details: {
        section_header: string;
        details: {
            label: string;
            values: string[];
        }[];
    }[];
    image_url: string | undefined;
}

interface Props {
    characterDetails: CharacterDetails;
}

export default function GetCharacterDetails({ characterDetails }: Props) {
    const { details, image_url } = characterDetails;
    const [viewDetails, setViewDetails] = useState(false);

    const onClick = () => {
        setViewDetails(!viewDetails);
    };

    return (
        <div className=' mb-8'>
            {image_url && (
                <div className='flex flex-col items-center justify-center h-[18rem] overflow-hidden'>
                    <div className='max-h-full max-w-full flex items-center'>
                        <Image
                            src={image_url}
                            alt="Character Image"
                            width={200}
                            height={200}
                            layout="intrinsic"
                            objectFit="contain"
                            className="custom-image"
                        />
                    </div>
                </div>
            )}
            {viewDetails ? (
                <div className='flex flex-col items-center '>
                    <button onClick={onClick} className='text-red-500 text-sm p-2'>Hide Details</button>
                    <div className='w-[16rem]'>
                        {details.map((section, index) => (
                            <div key={index}>
                                <div className='bg-neutral-700 p-1 flex flex-col items-center'>
                                    <h2 className='text-xs font-semibold'>{section.section_header}</h2>
                                </div>
                                {section.details.map((detail, idx) => (
                                    <div key={idx} className={`flex text-xs text-black p-1  ${idx % 2 === 0 ? 'bg-neutral-300' : 'bg-neutral-200'}`}>
                                        <div className='w-[50%] ml-2 flex flex-col justify-center'>
                                            <h3 className='font-semibold'>{detail.label}:</h3>
                                        </div>
                                        <div className='w-[50%] mr-2'>
                                            <ul>
                                                {detail.values.map((val, i) => (
                                                    <li key={i}>• {val}</li>
                                                ))}
                                            </ul>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        ))}
                    </div>
                </div>
            ) : (
                <div className='flex flex-col items-center'>
                    <button onClick={onClick} className='text-blue-500 text-sm p-2'>View Details</button>
                </div>
            )}
        </div>
    );
}
