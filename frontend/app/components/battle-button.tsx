"use client"
import React from "react";

export default function BattleButton() {
    return (
        <button className="mt-3 primary-btn h-10 text-lg bg-red-600 p-3 rounded-2xl font-semibold
        flex items-center justify-center 
        disabled:bg-neutral-400 
        disabled:text-neutral-300 
        disabled:cursor-not-allowed">
            Battle
        </button>
    );
}


