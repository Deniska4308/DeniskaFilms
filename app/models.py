from sqlalchemy import Column, Integer, String, Date, SmallInteger, Boolean, Table, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import date

#звʼязувальні таблиці
movie_genre = Table(
    "moviegenre",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id", ondelete="CASCADE"), primary_key=True),
    Column("genre_id", ForeignKey("genre.id", ondelete="CASCADE"), primary_key=True)
)

movie_actor = Table(
    'movieactor',
    Base.metadata,
    Column('movie_id', ForeignKey('movie.id', ondelete="CASCADE"), primary_key=True),
    Column('actor_id', ForeignKey('actor.id', ondelete='CASCADE'), primary_key=True)
)

movie_director = Table(
    'moviedirector',
    Base.metadata,
    Column('movie_id', ForeignKey('movie.id', ondelete="CASCADE"), primary_key=True),
    Column('director_id', ForeignKey('director.id', ondelete="CASCADE"), primary_key=True)
)

movie_country = Table(
    'moviecountry',
    Base.metadata,
    Column('movie_id', ForeignKey('movie.id', ondelete="CASCADE"), primary_key=True),
    Column('country_id', ForeignKey('country.id', ondelete="CASCADE"), primary_key=True)
)
# 10/10 таблиць

#фільм
class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(64), index=True, unique=True, nullable=False)
    original_title = Column(String(64), index=True, nullable=False)
    description = Column(Text, nullable=True)
    release_date = Column(Date, nullable=True)
    runtime = Column(SmallInteger, nullable=True)
    age_rating = Column(SmallInteger, nullable=False)
    deniska_rating = Column(SmallInteger, nullable=False)
    is_seria = Column(Boolean, nullable=False)
    poster_url = Column(Text, nullable=True)
    background_poster = Column(Text, nullable=True)
    created_at = Column(Date, nullable=False, default=date.today)

    #звʼязки до фільмів   
    # назва = relationship('назва_моделі(назва класу а не таблиці у sql)', secondary=Назва_звʼязувальної_таблиці, back_populates='нзва_протилежгого_звʼязка',lazy="...")
    genres = relationship( 
        'Genre',
        secondary=movie_genre,
        back_populates='movies', #назва 'назва' = relationship(...) у класі Genre
        lazy='selectin'
    )

    actors = relationship(
        'Actor',
        secondary=movie_actor,
        back_populates='movies',
        lazy='selectin'
    )

    directors = relationship(
        'Director',
        secondary=movie_director,
        back_populates='movies',
        lazy='selectin'
    )
    countries = relationship(
        'Country',
        secondary=movie_country,
        back_populates='movies',
        lazy='selectin'
    )
    roles = relationship(
        'Role',
        back_populates='movie',
        lazy='selectin'
    )


#жанри
class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(64), index=True, unique=True, nullable=False)

    movies = relationship(
        'Movie',
        secondary=movie_genre, #така як у movie
        back_populates='genres', #назва genres = relationship(...) у класі Movie
        lazy='selectin'
    )


#актори
class Actor(Base):
    __tablename__ = 'actor'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(64), unique=True, index=True, nullable=False)
    true_name = Column(String(64), index=True, nullable=False)
    birth_date = Column(Date, index=True, nullable=True)
    photo_url = Column(Text, nullable=True)

    movies = relationship(
        'Movie',
        secondary=movie_actor,
        back_populates='actors',
        lazy='selectin'
    )

#режисер
class Director(Base):
    __tablename__ = 'director'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(64), unique=True, index=True, nullable=False)
    true_name = Column(String(64), index=True, nullable=False)
    birth_date = Column(Date, index=True, nullable=True)
    photo_url = Column(Text, nullable=True)

    movies = relationship(
        'Movie',
        secondary=movie_director,
        back_populates='directors',
        lazy='selectin'
    )

class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(64), index=True, nullable=False)

    movies = relationship(
        'Movie',
        secondary=movie_country,
        back_populates='countries',
        lazy='selectin'
    )

class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    movie_id = Column(Integer, ForeignKey('movie.id', ondelete="CASCADE"))
    actor_id = Column(Integer, ForeignKey('actor.id', ondelete="CASCADE"))
    role_name = Column(String(64), nullable=False)

    #Звяʼзки
    movie = relationship('Movie', back_populates='roles')
    actors = relationship('Actor', backref='roles')