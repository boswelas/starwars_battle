# from char_image_scrape import scrape_char_image
# from chat_response import chat_response
# from char_detail_scrape import get_char_details
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from prisma import Prisma
# from battle_calculator import battle
# import asyncio



# app = Flask(__name__)
# # CORS(app, resources={r"/*": {"origins": "https://starwars-battle.vercel.app"}})
# CORS(app, resources={r"/*": {"origins": "*"}})


# db = Prisma()

    
# @app.route('/fetch_all_char', methods=['GET', 'OPTIONS'])
# async def fetch_characters():
#     try:
#         await db.connect()
#         char_data = await db.character.find_many()
#         char_names = [char.name for char in char_data]
#         char_names.sort()
 
#     except Exception as e:
#         print(f"Error retrieving all characters: {e}")
#         return jsonify(error="Internal server error"), 500
#     finally:
#         await db.disconnect()
#     return jsonify(char_names)  

# @app.route('/fetch_char', methods=['GET', 'OPTIONS'])
# async def fetch_character():
#     char_name = request.args.get('char_name')
#     if not char_name:
#         return jsonify(error="Character name is required"), 400
#     try:
#         await db.connect()
#         char_data = await db.character.find_first(
#             where={
#                 'name': char_name
#             }
#         )
#         if not char_data:
#             return jsonify(error="Character not found"), 404
#         char_data_dict = char_data.dict()
#     except Exception as e:
#         print(f"Error fetching character {char_name}: {e}")
#         return jsonify(error="Internal server error"), 500
#     finally:
#         await db.disconnect()
#     return jsonify(data=char_data_dict)

# @app.route('/get_char_deets', methods=['GET', 'OPTIONS'])
# async def get_details():
#     char_name = request.args.get('char_name')
#     if char_name:
#         char_details = await get_char_details(char_name)
#         if char_details:
#             return jsonify(data=char_details)
#         return jsonify(error="Character details not found"), 404
#     return jsonify(error="No character name provided"), 400

# @app.route('/get_char_image', methods=['GET', 'OPTIONS'])
# async def get_image():
#     char_name = request.args.get('char_name')
#     if not char_name:
#         return jsonify(error="Character name is required"), 400

#     await db.connect()
#     try:
#         char_data = await db.character.find_first(
#             where={
#                 'name': char_name
#             },
#         )
#         if not char_data:
#             return jsonify(error="Character image not found"), 404
#     except Exception as e:
#         print(f"Error fetching character {char_name}: {e}")
#         return jsonify(error="Internal server error"), 500
#     finally:
#         await db.disconnect()
#     return jsonify(data=char_data.image)

# @app.route('/character_battle', methods=['GET', 'OPTIONS'])
# async def get_battle():
#     character1 = request.args.get('character1')
#     character2 = request.args.get('character2')

#     if not (character1 and character2):
#         return jsonify(error="Characters are required"), 400
#     try:
#         await db.connect()
#         char1_data = await db.character.find_first(where={'name': character1})
#         if not char1_data:
#             return jsonify(error="Character1 not found"), 404
#         char2_data = await db.character.find_first(where={'name': character2})
#         if not char2_data:
#             return jsonify(error="Character2 not found"), 404
#         calculate_battle = battle(char1_data, char2_data)
#         battle_details = chat_response(calculate_battle)
#         battle_all = [[calculate_battle], [battle_details]]
#     except Exception as e:
#         print(f"Error fetching characters: {e}")
#         return jsonify(error="Internal server error"), 500
#     finally:
#         await db.disconnect()
#     return jsonify(data=battle_all)

# @app.route('/scrape_image', methods=['GET', 'OPTIONS'])
# async def get_scrape_image():
#     char_name = request.args.get('char_name')
#     if char_name:
#         image = await scrape_char_image(char_name)
#         if image:
#             return jsonify(data=image)
#         return jsonify(error="Character details not found"), 404
#     return jsonify(error="No character name provided"), 400

    

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

from char_image_scrape import scrape_char_image
from chat_response import chat_response
from char_detail_scrape import get_char_details
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras
from battle_calculator import battle

load_dotenv()

app = Flask(__name__)
cors = CORS(app, origins="*") 

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.DictCursor)
    return conn

@app.route('/fetch_all_char', methods=['GET', 'OPTIONS'])
@cross_origin()
def fetch_characters():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT name FROM Character")
        char_data = cur.fetchall()
        char_names = sorted([char['name'] for char in char_data])
    except Exception as e:
        print(f"Error retrieving all characters: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        conn.close()
    return jsonify(char_names)

@app.route('/fetch_char', methods=['GET', 'OPTIONS'])
@cross_origin()
def fetch_character():
    char_name = request.args.get('char_name')
    if not char_name:
        return jsonify(error="Character name is required"), 400
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Character WHERE name = %s", (char_name,))
        char_data = cur.fetchone()
        if not char_data:
            return jsonify(error="Character not found"), 404
        char_data_dict = dict(char_data)
    except Exception as e:
        print(f"Error fetching character {char_name}: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        conn.close()
    return jsonify(data=char_data_dict)

@app.route('/get_char_deets', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_details():
    char_name = request.args.get('char_name')
    if char_name:
        char_details = get_char_details(char_name) 
        if char_details:
            return jsonify(data=char_details)
        return jsonify(error="Character details not found"), 404
    return jsonify(error="No character name provided"), 400

@app.route('/get_char_image', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_image():
    char_name = request.args.get('char_name')
    if not char_name:
        return jsonify(error="Character name is required"), 400
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT image FROM Character WHERE name = %s", (char_name,))
        char_data = cur.fetchone()
        if not char_data:
            return jsonify(error="Character image not found"), 404
    except Exception as e:
        print(f"Error fetching character {char_name}: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        conn.close()
    return jsonify(data=char_data['image'])

@app.route('/character_battle', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_battle():
    character1 = request.args.get('character1')
    character2 = request.args.get('character2')

    if not (character1 and character2):
        return jsonify(error="Characters are required"), 400
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Character WHERE name = %s", (character1,))
        char1_data = cur.fetchone()
        if not char1_data:
            return jsonify(error="Character1 not found"), 404
        cur.execute("SELECT * FROM Character WHERE name = %s", (character2,))
        char2_data = cur.fetchone()
        if not char2_data:
            return jsonify(error="Character2 not found"), 404
        calculate_battle = battle(char1_data, char2_data)
        battle_details = chat_response(calculate_battle)
        battle_all = [[calculate_battle], [battle_details]]
    except Exception as e:
        print(f"Error fetching characters: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        conn.close()
    return jsonify(data=battle_all)

@app.route('/scrape_image', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_scrape_image():
    char_name = request.args.get('char_name')
    if char_name:
        image = scrape_char_image(char_name)  
        if image:
            return jsonify(data=image)
        return jsonify(error="Character details not found"), 404
    return jsonify(error="No character name provided"), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
