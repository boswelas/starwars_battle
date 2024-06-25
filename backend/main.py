from chat_response import chat_response
from char_detail_scrape import get_char_details
from flask import Flask, jsonify, request
from flask_cors import CORS
from prisma import Prisma
from battle_calculator import battle


app = Flask(__name__)
CORS(app)

# Initialize Prisma Client
db = Prisma()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/fetch_all_char', methods=['GET'])
async def fetch_characters():
    try:
        await db.connect()
        char_data = await db.character.find_many()
        char_names = [char.name for char in char_data]
        char_names.sort()
 
    except Exception as e:
        print(f"Error retrieving all characters: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        await db.disconnect()
    return jsonify(char_names)  

@app.route('/fetch_char', methods=['GET'])
async def fetch_character():
    char_name = request.args.get('char_name')
    if not char_name:
        return jsonify(error="Character name is required"), 400

    await db.connect()
    try:
        char_data = await db.character.find_first(
            where={
                'name': char_name
            }
        )
        if not char_data:
            return jsonify(error="Character not found"), 404
        char_data_dict = char_data.dict()
    except Exception as e:
        print(f"Error fetching character {char_name}: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        await db.disconnect()
    return jsonify(data=char_data_dict)

@app.route('/get_char_deets', methods=['GET'])
async def get_details():
    char_name = request.args.get('char_name')
    if char_name:
        char_details = await get_char_details(char_name)
        if char_details:
            return jsonify(data=char_details)
        return jsonify(error="Character details not found"), 404
    return jsonify(error="No character name provided"), 400

@app.route('/get_char_image', methods=['GET'])
async def get_image():
    char_name = request.args.get('char_name')
    if not char_name:
        return jsonify(error="Character name is required"), 400

    await db.connect()
    try:
        char_data = await db.character.find_first(
            where={
                'name': char_name
            },
        )
        if not char_data:
            return jsonify(error="Character image not found"), 404
    except Exception as e:
        print(f"Error fetching character {char_name}: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        await db.disconnect()
    return jsonify(data=char_data.image)

@app.route('/character_battle', methods=['GET'])
async def get_battle():
    character1 = request.args.get('character1')
    character2 = request.args.get('character2')

    if not (character1 and character2):
        return jsonify(error="Characters are required"), 400
    try:
        await db.connect()
        char1_data = await db.character.find_first(where={'name': character1})
        if not char1_data:
            return jsonify(error="Character1 not found"), 404
        char2_data = await db.character.find_first(where={'name': character2})
        if not char2_data:
            return jsonify(error="Character2 not found"), 404
        calculate_battle = battle(char1_data, char2_data)
        battle_details = chat_response(calculate_battle)
    except Exception as e:
        print(f"Error fetching characters: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        await db.disconnect()
    return jsonify(data=battle_details)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
