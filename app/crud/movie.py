from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from models import Movie

async def get_movie_by_id(db: AsyncSession, movie_id: int):
    """
    повертає список з фільмом і всіма акторами, режисерами, країнама і ролями

    :param db:
    :param movie_id:
    :return:
    """
    result = await db.execute(
        select(Movie)
        .options(
            selectinload(Movie.actors),
            selectinload(Movie.directors),
            selectinload(Movie.countries)
        )
        .where(Movie.id == movie_id)
    )
    return result.scalars().first()
