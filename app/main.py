
# Libraries
from fastapi import FastAPI, HTTPException
from routers import races


# Application
app = FastAPI()


# Include Routers => Blueprints
app.include_router(races.router)
