from flask import Flask, jsonify, request
from flask_cors import CORS
from prisma import Prisma

app = Flask(__name__)
CORS(app)

# Initialize Prisma Client
db = Prisma()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/character', methods=['GET'])
async def get_character():
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


@app.route('/fetch_all_char', methods=['GET'])
async def fetch_characters():
    try:
        await db.connect()
        char_data = await db.character.find_many()
        char_names = [char.name for char in char_data] 
    except Exception as e:
        print(f"Error retrieving all characters: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        await db.disconnect()
    return jsonify(char_names)  

@app.route('/fetch_char', methods=['GET'])
async def fetch_character(name):
    try:
        await db.connect()
        char_data = await db.character.find_first(
            where={
                'name':name
            }
        )
    except Exception as e:
        print(f"Error retrieving all characters: {e}")
        return jsonify(error="Internal server error"), 500
    finally:
        await db.disconnect()
    print(char_data)
    return jsonify(char_data) 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
