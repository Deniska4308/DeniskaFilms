from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, Query
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas import MovieDetail, Movie
from app.database import get_db
from app.crud.movie import get_movie_by_id, get_dubbing_byId, get_movie_list, movie_by_slug
from app.utils.security import decode_jwt
import os

router = APIRouter(
    prefix="/api",
    tags=["api"]
)

@router.get("/movie/{slug}", response_model=MovieDetail)
async def get_movie_by_slug(slug: str, db: AsyncSession = Depends(get_db)):
    movie_data = await movie_by_slug(db, slug)
    if not  movie_data:
        raise HTTPException(status_code=404, detail="Movie not found(")
    return movie_data

@router.get("/movielist", response_model=List[Movie])
async def get_movies_list(skip: int = Query(0, ge=0),
                         limit: int = Query(30, ge=1, le=120),
                         db: AsyncSession = Depends(get_db)):
        movies = await get_movie_list(db, skip, limit)

        if not movies:
            raise HTTPException(status_code=404, detail="Not Found")

        return movies

#видає файл по ід озвучки
@router.get("/movie/view/{dubbing_id}")
async def view_movie(dubbing_id: int, request: Request, db: AsyncSession = Depends(get_db)):
    #тут треба захистити
    user_cookie = decode_jwt(request) #тут треба ще звірку з базою
    file_name = await get_dubbing_byId(db, dubbing_id)
    movie_path = os.path.join('app/view/movies', file_name)

    if not os.path.exists(movie_path):
        raise HTTPException(status_code=404, detail="movie not found")

    if user_cookie and user_cookie["role"] in ["allowed", "admin"]:
        return FileResponse(movie_path, media_type="video/mp4")
    else:
        raise HTTPException(status_code=404, detail="not allowed")
