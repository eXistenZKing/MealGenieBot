# from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import api_router


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield


app = FastAPI(
    title="MealGenie",
    # lifespan=lifespan
    )

app.include_router(api_router)
