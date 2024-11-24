import asyncio
import os
from random import randint

import logfire
import openai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query, status

from ch6_fastapi_utils import (
    Genre, get_books_by_genre, get_recommendations, get_top_10
)
from database import books as books_db

load_dotenv()

app = FastAPI(title="Bookstore API", version="0.1")
client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

logfire.configure(service_name="bookstore", metrics=True)
logfire.instrument_fastapi(app)
logfire.instrument_openai(client)


@app.get("/top-10")
async def top_10() -> list[dict]:
    return await get_top_10(books_db)


@app.get("/books")
async def get_books(
    limit: int = 10, genre: list[Genre] = Query(None)
) -> list[dict]:
    if limit > 100:
        raise ValueError("Limit should be less than or equal to 100")
    return await get_books_by_genre(books_db, genre, limit)


@app.get("/unreliable_endpoint")
async def unreliable_endpoint() -> None:
    id = randint(1, 6)
    logfire.info("Random ID: {id}", id=id)
    match id:
        case 5:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        case 4:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        case 3:
            raise ValueError("Random error")
        case _:
            return None


@app.get("/recommendations")
async def recommendations(interests: str) -> str:
    return await get_recommendations(client, interests)


@app.get("/slow_endpoint")
async def slow_endpoint() -> None:
    time_to_sleep = randint(1, 2)
    await asyncio.sleep(time_to_sleep)
    return None
