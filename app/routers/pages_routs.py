from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import templates
from app.database import get_db
from app.crud.movie import get_movie_by_id, get_dubbingFor_movie
from app.utils.webSite import movieDatetime, movieRuntime, movieStars
from urllib.parse import urljoin
from app.utils.security import decode_jwt, show_player

router = APIRouter(
    tags=["page"]
)

@router.get("/movie/{movie_id}", response_class=HTMLResponse)
async def page_by_movie_id(movie_id: int, request: Request, db: AsyncSession = Depends(get_db)):
    # base_url = "http://127.0.0.1:8000"
    movie = await get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found(")

    movieDay, movieMonth, movieYear = movieDatetime(movie.release_date)
    full_stars, has_halfStar = movieStars(movie.deniska_rating)

    #можливо це треба перенести(це не риторика)
    def get_start_dubbing(data):
        start_dubbung = None
        for dub in data.dubbing:
            if dub.dubble_lang == 'ukr':
                start_dubbung = dub.id
        if not start_dubbung and data.dubbing:
            start_dubbung = data.dubbing[0].id
        return start_dubbung


    return templates.TemplateResponse("devmovie.html", {"request": request,
                                                     "title": movie.title,
                                                     "eng_title": movie.original_title,
                                                     "rating": movie.deniska_rating,
                                                     "age_rating": movie.age_rating,
                                                     "poster_url": movie.poster_url,
                                                     "movieDay": movieDay,
                                                     "movieMonth": movieMonth,
                                                     "movieYear": movieYear,
                                                     "runtime": movieRuntime(movie.runtime),
                                                     "full_stars": full_stars,
                                                     "has_halfStar": has_halfStar,
                                                     "countries": movie.countries,
                                                     "description": movie.description,
                                                     "genres": movie.genres,
                                                     "actors": movie.actors,
                                                     "directors": movie.directors,
                                                     "show_player": show_player(request),
                                                     "dubbing": movie.dubbing,
                                                     "start_dub": get_start_dubbing(movie)
                                                     })

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

#для перевірки авторизації (тимчасово)
@router.get("/auth/test", response_class=HTMLResponse)
async def test(request: Request):
    data = decode_jwt(request)
    if not data:
        mess = "не авторизований"
    else:
        mess = f"Авторизований!! Твоя роль [{data['role']}]"
    return templates.TemplateResponse("test.html", {"request": request,
                                                    "mess": mess,
                                                    "show_player": show_player(request)})