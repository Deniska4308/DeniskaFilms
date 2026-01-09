from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas import MovieDetail, ActorOut, ActorIn
from app.database import get_db
from app.crud.movie import get_movie_by_id, pos_actor, get_dubbing_byId
from app.utils.security import decode_jwt
from sqlalchemy.exc import IntegrityError
import os

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

#видає файл по ід озвучки
@router.get("/view/{dubbing_id}")
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