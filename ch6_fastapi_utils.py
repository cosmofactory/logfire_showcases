from enum import Enum

import logfire
from openai import OpenAI

from database import book_titles


class Genre(Enum):
    ADVENTURE = "Adventure"
    HISTORICAL_FICTION = "Historical Fiction"
    PHILOSOPHICAL_FICTION = "Philosophical Fiction"
    TRAGEDY = "Tragedy"
    ROMANCE = "Romance"
    SCIENCE_FICTION = "Science Fiction"
    DRAMA = "Drama"
    SATIRE = "Satire"
    MAGIC_REALISM = "Magic Realism"
    PSYCHOLOGICAL_FICTION = "Psychological Fiction"


@logfire.instrument()
async def get_top_10(books: list[dict]) -> list[dict]:
    return sorted(books, key=lambda x: x["rank"])[:10]


@logfire.instrument()
async def get_books_by_genre(
    books: list[dict], genre: list[Genre] | None, limit: int
) -> list[dict]:
    """
    Retrieve a list of books filtered by genre.

    Args:
        books (list[dict]): A list of book dictionaries.
        genre (list[Genre] | None): A list of genres to filter by.
         If None, no filtering is applied.
        limit (int): The maximum number of books to return.

    Returns:
        list[dict]: A list of books filtered by the specified genres, limited
          to the specified number.
    """
    result = []
    if genre:
        for book in books:
            for genres in book["data"]["genre"]:
                for i in genre:
                    if i.value in genres:
                        result.append(book)
    else:
        result = books
    return result[:limit]


async def get_recommendations(client: OpenAI, interests: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant in an online bookstore. "
                    f"The following books are available: {book_titles}. "
                    "When a customer asks for a recommendation "
                    "and provides their interests, "
                    "you should recommend books from the collection "
                    "that match their preferences."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Recommend me a good book. I'm interested in {interests}."
                ),
            },
        ],
    )
    return completion.choices[0].message.content.strip()
