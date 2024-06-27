import { battle } from '../apis/api';

export async function getBattle(char1: string, char2: string) {
    const battle_details = battle(char1, char2);
    console.log(battle_details);
    return battle_details;
}
