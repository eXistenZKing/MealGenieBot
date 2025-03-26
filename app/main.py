from fastapi import FastAPI

from app.api import api_router


app = FastAPI(title="MealGenie")

app.include_router(api_router)
