from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ['GPT_PASSWORD']
client = OpenAI(api_key=API_KEY)

def chat_response(battle):
    battle_deets=[]
    battle_deets.append(battle[0])
    battle_deets.append(f"{battle[-1]} is the winner")
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": f"write a creative story with setting, weapons, battle to death or KO. maximum 8 sentences. {battle_deets}",
        }
    ])
    return response.choices[0].message.content

