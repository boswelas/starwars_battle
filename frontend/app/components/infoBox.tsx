import React, { useState } from 'react';
import { XMarkIcon } from "@heroicons/react/24/solid";


type InfoBoxProps = {
    onClose: () => void;
};

export default function InfoBox({ onClose }: InfoBoxProps) {
    const [isOpen, setIsOpen] = useState(true);

    const handleClose = () => {
        setIsOpen(false);
        onClose();
    };

    return (
        <div className={`fixed top-6 left-6 bg-neutral-200 w-[20rem] p-4 shadow-md z-50 ${isOpen ? 'block' : 'hidden'}`}>
            <div className="flex justify-between items-center">
                <button onClick={handleClose} className="text-black absolute right-1 top-2">
                    <XMarkIcon className="size-5" /></button>
            </div>
            <div className='text-black mt-[.5rem] text-sm'>
                <ul>
                    <li>• Characters take a moment to load because they are scraped in real time from <a href='https://starwars.fandom.com/' target="_blank" className='text-blue-700 underline'>starwars.fandom.com</a></li>
                    <li>• The battle narrative is generated with ChatGPT's API.</li>
                    <li className='mt-3'>• Like my project? Think about employing me!  <a href='https://boswelas.github.io/' target="_blank" className='text-blue-700 underline'>My Portfolio</a></li>
                </ul>
            </div>
        </div>
    );
};
