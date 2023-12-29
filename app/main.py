
# Libraries
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv, dotenv_values
import requests
import json


# Application
app = FastAPI()


# Router Race
# router = APIRouter(prefix='/races',
#                    tags=['Race'])


# List all races
@app.get("/all")
async def read_all_races():

    characters_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl'

    api_token = dotenv_values(".env")

    characters_request = requests.get(characters_endpoint, headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'})

    characters = json.loads(characters_request.content)['docs']

    all_races = []
    for i in characters:
        race = i['race']
        if race not in all_races and race != '':
            all_races.append(race)

    if characters:
        return all_races

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )
