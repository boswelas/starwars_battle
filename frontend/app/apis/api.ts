const API_URL = "https://starwarsbattle-production.up.railway.app"
// const API_URL = "http://127.0.0.1:5000"

export const fetchAllCharacters = async (): Promise<string[]> => {
    try {
        const response = await fetch(`${API_URL}/fetch_all_char`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        if (Array.isArray(data) && data.every(item => typeof item === 'string')) {
            return data;
        } else {
            console.error('Data is not an array of strings:', data);
            return [];
        }
    } catch (error) {
        console.error('Error fetching all characters:', error);
        return [];
    }
};

export const fetchCharacter = async (char_name: string): Promise<any> => {
    try {
        const response = await fetch(`${API_URL}/fetch_char?char_name=${encodeURIComponent(char_name)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching character data:', error);
        return { error: 'Error fetching character data' };
    }
};

export const battle = async (character1: string, character2: string): Promise<any> => {
    try {
        const response = await fetch(`${API_URL}/character_battle?character1=${encodeURIComponent(character1)}&character2=${encodeURIComponent(character2)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching all characters:', error);
        return [];
    }
};

export const fetchCharacterDetails = async (char_name: string): Promise<any> => {
    try {
        const response = await fetch(`${API_URL}/get_char_deets?char_name=${encodeURIComponent(char_name)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log("data: ", data);
        return data;
    } catch (error) {
        console.error('Error fetching all characters:', error);
        return [];
    }
};

export const getCharImage = async (char_name: string): Promise<any> => {
    try {
        const response = await fetch(`${API_URL}/get_char_image?char_name=${encodeURIComponent(char_name)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching all characters:', error);
        return [];
    }
};

export const battle_calc = async (character1: string, character2: string): Promise<any> => {
    try {
        const response = await fetch(`${API_URL}/calculate_battle?character1=${encodeURIComponent(character1)}&character2=${encodeURIComponent(character2)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching all characters:', error);
        return [];
    }
};

export const scrapeCharImage = async (char_name: string): Promise<any> => {
    try {
        const response = await fetch(`${API_URL}/scrape_image?char_name=${encodeURIComponent(char_name)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching all characters:', error);
        return [];
    }
};
