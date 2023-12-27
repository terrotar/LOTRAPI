
# Libraries
from fastapi import FastAPI
from dotenv import load_dotenv


# Application
app = FastAPI()



load_dotenv()


# Router Race
# router = APIRouter(prefix='/races',
#                    tags=['Race'])


# List all races
@app.get("/all")
async def read_all_races(races: list):

    all_races = 'url'

    return all_races

    # if app_poke:
    #     return app_poke

    # raise HTTPException(
    #     status_code=400,
    #     detail="Database is empty"
    # )

