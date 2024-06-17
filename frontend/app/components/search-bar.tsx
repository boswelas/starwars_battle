import { Autocomplete, AutocompleteItem } from "@nextui-org/autocomplete";
import React from "react";

interface SearchBarProps {
    names: string[];
    onChange: (value: string) => void;
}

export default function SearchBar({ names, onChange }: SearchBarProps) {
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        onChange(event.target.value);
    };

    return (
        <div className="flex w-full flex-wrap md:flex-nowrap gap-4 text-black">
            <Autocomplete
                label="Choose a character"
                className="max-w-xs"
                onChange={handleChange} // Adjusted to handle event
            >
                {names.map((name) => (
                    <AutocompleteItem key={name} value={name} className="text-black">
                        {name}
                    </AutocompleteItem>
                ))}
            </Autocomplete>
        </div>
    );
}
