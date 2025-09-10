from pydantic import BaseModel
from datetime import date
from typing import Optional
from typing import List

class Movie(BaseModel):
    id: int
    title: str
    original_title: str
    description: str
    release_date: date
    runtime: int
    age_rating: int
    deniska_rating: int
    is_seria: bool
    poster_url: Optional[str]
    background_poster: Optional[str]
    created_at: Optional[date]

class ActorOut(BaseModel):
    id: int
    name: str
    true_name: str
    birth_date: Optional[date]
    photo_url: Optional[str]
    is_female: bool

    class Config:
        from_attributes = True

class ActorIn(BaseModel):
    name: str
    true_name: str
    birth_date: date | None = None
    photo_url: str | None = None
    is_female: bool

class Director(BaseModel):
    id: int
    name: str
    true_name: str
    birth_date: Optional[date]
    photo_url: Optional[str]
    is_female: bool

    class Config:
        from_attributes = True

class Country(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class Role(BaseModel):
    id: int
    movie_id: int
    actor_id: int
    role_name: str

    class Config:
        from_attributes = True

#=================================Додаткові таблиці==================================
#для повної інфи про фільм
class MovieDetail(Movie):
    actors: List[ActorOut]
    directors: List[Director]
    countries: List[Country]


