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

class Actor(BaseModel):
    id: int
    name: str
    true_name: str
    birth_date: Optional[date]
    photo_url: Optional[str]

    class Config:
        from_attributes = True

class Director(BaseModel):
    id: int
    name: str
    true_name: str
    birth_date: Optional[date]
    photo_url: Optional[str]

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
    actors: List[Actor]
    directors: List[Director]
    countries: List[Country]


