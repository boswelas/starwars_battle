from prisma import Client as PrismaClient
from backend.char_stats_scrape import get_char_data
import asyncio

db = PrismaClient()

async def add_character_data():
    try:
        await db.connect()

        char_data = await get_char_data()

        for char in char_data:
            try:
                await db.character.create(
                    data={
                    'name': char['name'],
                    'image': char['image'],
                    'range': char['range'],
                    'base_atk': int(char['base_atk']),
                    'base_def': int(char['base_def']),
                    'max_atk': int(char['max_atk']),
                    'max_def': int(char['max_def']),
                    'acc': int(char['acc']),
                    'eva': int(char['eva']),
                    })
            except Exception as e:
                print(f"Error creating entry for {char['name']}: {e}")
    finally:
        await db.disconnect()
            
async def main():
    await add_character_data()

if __name__ == "__main__":
    asyncio.run(main())
