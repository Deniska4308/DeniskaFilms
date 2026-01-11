from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

#мої модулі
from app.routers import api_movie_routs, pages_routs, api_user_routs, auth
from app.core.config import static_dir


app = FastAPI(
	docs_url=None,
	redock_url=None,
	open_api=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://deniskafilms.com",
                   "https://www.deniskafilms.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_movie_routs.router)
app.include_router(pages_routs.router)
app.include_router(api_user_routs.router)
app.include_router(auth.router)

app.mount("/static", StaticFiles(directory=static_dir), name="static")