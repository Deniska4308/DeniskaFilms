from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.models import Movie, Actor, Dubbing
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
            selectinload(Movie.countries),
            selectinload(Movie.genres),
            selectinload(Movie.dubbing)
        )
        .where(Movie.id == movie_id)
    )
    return result.scalars().first()

async def get_movies_list(db: AsyncSession):
    """
    видає список фільмів
    """
    result = await db.execute(
        select(Movie)
    )
    return  result.scalars().all()

async def get_dubbingFor_movie(db: AsyncSession, movie_id: int):
    """
    Вибирає по id фільму список озвучок
    """
    result = await db.execute(
        select(Dubbing).where(Dubbing.movie_id == movie_id)
    )
    return result.scalars().all()

async def get_dubbing_byId(db: AsyncSession, dubbing_id: int):
    """
    Видає по id озвучки назву файлу у папці movies
    Видає один результат
    """
    result = await db.execute(
        select(Dubbing.movie_url).where(Dubbing.id == dubbing_id)
    )
    return result.scalars().first()

async def pos_actor(db: AsyncSession, data: ActorIn):
    """
    Добавляє актора
    На виході ActorOut
    """
    actor = Actor(
        name=data.name,
        true_name=data.true_name,
        birth_date=data.birth_date,
        photo_url=data.photo_url,
        is_female=data.is_female
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

async def get_actor(db = AsyncSession, limit: int = 10, offset: int = 0):
    result = await db.execute(
        select(Actor)
        .offset(offset)
        .limit(limit)
    )
    return result.scalars().all()