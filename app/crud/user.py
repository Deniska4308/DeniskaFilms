from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password

async def get_user_by_id(db: AsyncSession, user_id: int):
    """повертає всю інфу РАЗОМ З ПАРОЛЕМ"""
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    return result.scalars().first()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(
        select(User).where(User.username == username)
    )
    return result.scalars().first()

async def post_user(db: AsyncSession, data: UserCreate):
    """Постить юзера"""
    user = User(
        username=data.username,
        password_hash=hash_password(data.password)
    )
    db.add(user)
    try:
        await db.commit()#комітить зміни
    except IntegrityError:
        await db.rollback()#відкатує якщо щось не так
        raise
    await db.refresh(user)#оновлює таблицю для полів з дефолтними значенями
    return user


