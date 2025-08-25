from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import MovieDetail
from app.database import get_db
from app.crud.movie import get_movie_by_id

router = APIRouter(
    prefix="/api"
)

@router.get("/movie/{movie_id}", response_model=MovieDetail)
async def get_movie_by_MovieId(movie_id: int, db: AsyncSession = Depends(get_db)):
    movie_data = await get_movie_by_id(db, movie_id)
    if not  movie_data:
        raise HTTPException(status_code=404, detail="Movie not found(")
    return movie_data