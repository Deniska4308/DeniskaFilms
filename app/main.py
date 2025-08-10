from fastapi import FastAPI, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from urllib.parse import urljoin
#мої модулі
from utils.webSite import movieDatetime, movieRuntime, movieStars
from schemas import MovieDetail
from database import get_db
from crud.movie import get_movie_by_id

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "view/templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "view/static")), name="static")

@app.get('/testPage/{num}', response_class=HTMLResponse)
async def test_page_jinja(request: Request, num: int):
    return templates.TemplateResponse("test.html", {"request": request, "number": num})

@app.get('/movie', response_class=HTMLResponse)
async def test_page_jinja(request: Request,):
    return templates.TemplateResponse("movie.html", {"request": request})

@app.get('/movie/{movie_id}', response_class=HTMLResponse)
async def movie_page_by_id(movie_id, request: Request, db: AsyncSession = Depends(get_db)):
    base_url = 'http://127.0.0.1:8000'
    movie = await get_movie_by_id(db, int(movie_id))

    if not movie:
        raise HTTPException(status_code=404, detail='Фільм не знайдено')

    movieDay, movieMonth, movieYear = movieDatetime(movie.release_date)
    full_stars, has_halfStar = movieStars(movie.deniska_rating)

    return templates.TemplateResponse("movie.html", {"request": request,
                                                     "title": movie.title,
                                                     "eng_title": movie.original_title,
                                                     "rating": movie.deniska_rating,
                                                     "age_rating": movie.age_rating,
                                                     "poster_url": urljoin(base_url, movie.poster_url),
                                                     "movieDay": movieDay,
                                                     "movieMonth": movieMonth,
                                                     "movieYear": movieYear,
                                                     "runtime": movieRuntime(movie.runtime),
                                                     "full_stars": full_stars,
                                                     "has_halfStar": has_halfStar,
                                                     "countries": movie.countries
                                                     })

@app.get('/api/movie/{movie_id}', response_model=MovieDetail)
async def get_movies(movie_id: int, db: AsyncSession = Depends(get_db)):
    movie = await get_movie_by_id(db, movie_id)
    # for i in movie.countries:
    #     name = i.name
    #     print(name)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

