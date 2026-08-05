from slugify import slugify
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Movie

async def generate_unique_slug(title: str, db: AsyncSession) -> str:
    base_slug = slugify(title)
    slug = base_slug
    counter = 1

    #обробка для унікальності воно добавить цифру до результату [counter]
    while True:
        result = await db.execute(select(Movie).where(Movie.slug == slug))
        existing_movie = result.scalars().first()

        if not existing_movie:
            break

        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug