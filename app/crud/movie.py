from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.models import Movie, Actor
from app.schemas.schemas import ActorIn
from sqlalchemy.exc import IntegrityError

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

async def pos_actor(db: AsyncSession, data: ActorIn):
    """добавляє актора"""
    actor = Actor(
        name=data.name,
        true_name=data.true_name,
        birth_date=data.birth_date,
        photo_url=data.photo_url
    )
    db.add(actor)
    try:
        await db.commit()
    except IntegrityError as e:
        await db.rollback()
        if getattr(e.orig, "sqlstate", None) == "23505":
            return None
        raise
    await db.refresh(actor)
    return actor