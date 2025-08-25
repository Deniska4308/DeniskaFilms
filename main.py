from fastapi import FastAPI, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from urllib.parse import urljoin
#мої модулі
from app.utils.webSite import movieDatetime, movieRuntime, movieStars
from app.schemas import MovieDetail
from app.database import get_db
from app.crud.movie import get_movie_by_id
from app.routers import api_movie_routs, pages_routs
from app.core.config import static_dir


app = FastAPI()

app.include_router(api_movie_routs.router)
app.include_router(pages_routs.router)

app.mount("/static", StaticFiles(directory=static_dir), name="static")




