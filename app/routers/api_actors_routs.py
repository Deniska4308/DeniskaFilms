from fastapi import APIRouter, Depends, HTTPException, Request
from app.schemas.schemas import ActorOut
from app.database import get_db
from app.crud.movie import get_actor
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter(
    prefix="/api",
    tags=["api", "actor"]
)

@router.get("/actors", response_model=List[ActorOut])
async def get_actors(limit: int = 10, offset: int = 0, db: AsyncSession = Depends(get_db)):
    actors = await get_actor(db, limit, offset)
    return actors