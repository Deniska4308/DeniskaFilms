from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# Створюємо асинхронний двигун
engine = create_async_engine(DATABASE_URL, echo=False)

#фаботка сесій
asyncSession = sessionmaker (
    engine,
    expire_on_commit=True,
    class_=AsyncSession
)

#базовий клас для моделей
Base = declarative_base()

#залежність від fastapi
async def get_db():
    async with asyncSession() as session:
        yield session