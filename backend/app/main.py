import asyncio
import json
from char_image_scrape import scrape_char_image
from chat_response import chat_response
from char_detail_scrape import get_char_details
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras
from battle_calculator import battle

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://starwars-battle.vercel.app"}})

DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_PORT = 55863
DATABASE_NAME = os.getenv('DB_NAME')
DATABASE_USER = os.getenv('DB_USER')
DATABASE_PASSWORD = os.getenv('DB_PASS')



@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DATABASE_NAME, 
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )
    return conn

@app.route('/')
def index():
    print("Server is running!")
    return jsonify("Welcome to the backend!")

@app.route('/fetch_all_char', methods=['GET', 'OPTIONS'])
def fetch_characters():
    if request.method == 'OPTIONS':
        return '', 204 
    conn = get_db_connection()
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute('SELECT name FROM "Character"')
        char_data = cur.fetchall()
        char_names = sorted([char['name'] for char in char_data])
    except Exception as e:
        print(f"Error retrieving all characters: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        conn.close()
    return jsonify(char_names)

@app.route('/fetch_char', methods=['GET', 'OPTIONS'])
def fetch_character():
    if request.method == 'OPTIONS':
        return '', 204 
    char_name = request.args.get('char_name')
    if not char_name:
        return jsonify(error="Character name is required"), 400
    conn = get_db_connection()
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute('SELECT * FROM "Character" WHERE name = %s', (char_name,))
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
def get_details():
    if request.method == 'OPTIONS':
        return '', 204 
    char_name = request.args.get('char_name')
    if char_name:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute('SELECT * FROM "characterdata" WHERE name = %s', (char_name,))
        character = cur.fetchone()

        if character:
            conn.close()
            return jsonify(data=character)
      
        char_details = asyncio.run(get_char_details(char_name))
        if char_details:
            details_serialized = json.dumps(char_details['details'])
            if char_details.get('image_url'):                
                image_url = char_details['image_url'] 
                cur.execute('INSERT INTO "characterdata" (name, details, image_url) VALUES (%s, %s, %s)',
                            (char_name, details_serialized, image_url))
                conn.commit()
                cur.execute('SELECT * FROM "characterdata" WHERE name = %s', (char_name,))
                character = cur.fetchone()
                conn.close()
                return jsonify(data=character)
            return jsonify(data=char_details)
    return jsonify(error="No character name provided"), 400

@app.route('/get_char_image', methods=['GET', 'OPTIONS'])
def get_image():
    if request.method == 'OPTIONS':
        return '', 204 
    char_name = request.args.get('char_name')
    if not char_name:
        return jsonify(error="Character name is required"), 400
    conn = get_db_connection()
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute('SELECT image FROM "Character" WHERE name = %s', (char_name,))
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
def get_battle():
    if request.method == 'OPTIONS':
        return '', 204 
    character1 = request.args.get('character1')
    character2 = request.args.get('character2')
    if not (character1 and character2):
        return jsonify(error="Characters are required"), 400
    conn = get_db_connection()
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute('SELECT * FROM "Character" WHERE name = %s', (character1,))
        char1_data = cur.fetchone()
        if not char1_data:
            return jsonify(error="Character1 not found"), 404
        cur.execute('SELECT * FROM "Character" WHERE name = %s', (character2,))
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
def get_scrape_image():
    if request.method == 'OPTIONS':
        return '', 204 
    char_name = request.args.get('char_name')
    if char_name:
        image = asyncio.run(scrape_char_image(char_name))  
        if image:
            return jsonify(data=image)
        return jsonify(error="Character details not found"), 404
    return jsonify(error="No character name provided"), 400



# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
