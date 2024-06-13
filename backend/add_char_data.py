from prisma import Client as PrismaClient
from char_data_scrape import get_char_data
import asyncio


async def add_character_data():
    try:
        prisma = PrismaClient()
        await prisma.connect()

        char_data = await get_char_data()

        for char in char_data:
            try:
                await prisma.character.create(
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
        await prisma.disconnect()
            
async def main():
    await add_character_data()

if __name__ == "__main__":
    asyncio.run(main())
