from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas import MovieDetail, ActorOut, ActorIn
from app.database import get_db
from app.crud.movie import get_movie_by_id, pos_actor
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/api/movie",
    tags=["api"]
)

@router.get("/{movie_id}", response_model=MovieDetail)
async def get_movie_by_MovieId(movie_id: int, db: AsyncSession = Depends(get_db)):
    movie_data = await get_movie_by_id(db, movie_id)
    if not  movie_data:
        raise HTTPException(status_code=404, detail="Movie not found(")
    return movie_data

@router.post("/actor", response_model=ActorOut, tags=["admin"], status_code=201)
async def post_actor(payload: ActorIn, db: AsyncSession = Depends(get_db)):
    actor = await pos_actor(db, payload)
    if actor is None:
        raise  HTTPException(status_code=409, detail="Actor already exists")
    return actor