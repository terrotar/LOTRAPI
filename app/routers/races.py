
# Libraries
from fastapi import HTTPException, APIRouter
from dotenv import dotenv_values
import requests
import json


# Router Races
router = APIRouter(prefix='/races',
                   tags=['Race'])


# List all races
@router.get("/all")
async def list_all_races():

    characters_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=characters_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

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


# List all Human
@router.get("/human")
async def list_all_human():

    human_endpoint = 'https://the-one-api.dev/v2/character?race=Human&wikiUrl'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=human_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

    all_humans = json.loads(characters_request.content)['docs']

    return all_humans
    if all_humans:
        return all_humans

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )


# List all Elf
@router.get("/elf")
async def list_all_elf():

    human_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl&race=Elf'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=human_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

    all_elfs = json.loads(characters_request.content)['docs']

    if all_elfs:
        return all_elfs

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )


# List all Dwarf
@router.get("/dwarf")
async def list_all_dwarf():

    human_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl&race=Dwarf'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=human_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

    all_dwarfs = json.loads(characters_request.content)['docs']

    if all_dwarfs:
        return all_dwarfs

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )


# List all Hobbit
@router.get("/hobbit")
async def list_all_hobbit():

    human_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl&race=Hobbit'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=human_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

    all_hobbits = json.loads(characters_request.content)['docs']

    if all_hobbits:
        return all_hobbits

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )


# List all Maiar
@router.get("/maiar")
async def list_all_maiar():

    human_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl&race=Maiar'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=human_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

    all_amiar = json.loads(characters_request.content)['docs']

    if all_amiar:
        return all_amiar

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )


# List all Ent
@router.get("/ent")
async def list_all_ent():

    human_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl&race=Ent'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=human_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

    all_ent = json.loads(characters_request.content)['docs']

    if all_ent:
        return all_ent

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )


# List all Men
@router.get("/men")
async def list_all_men():

    human_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl&race=Men'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=human_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

    all_men = json.loads(characters_request.content)['docs']

    if all_men:
        return all_men

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )


# List all Orc
@router.get("/orc")
async def list_all_orc():

    human_endpoint = 'https://the-one-api.dev/v2/character?wikiUrl&race=Orc'

    api_token = dotenv_values(".env")

    characters_request = requests.get(
        url=human_endpoint,
        headers={'Authorization': f'Bearer {api_token['THE_ONE_API_TOKEN']}'}
    )

    all_orcs = json.loads(characters_request.content)['docs']

    if all_orcs:
        return all_orcs

    raise HTTPException(
        status_code=503,
        detail="The One API connection failed"
    )
