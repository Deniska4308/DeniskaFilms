from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

#мої модулі

from app.routers import api_movie_routs, pages_routs, api_user_routs, auth
from app.core.config import static_dir


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "null" #для фронта з файлу просто
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_movie_routs.router)
app.include_router(pages_routs.router)
app.include_router(api_user_routs.router)
app.include_router(auth.router)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

