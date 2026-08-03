from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    Table,
    Text,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


# звʼязувальні таблиці

movie_genre = Table(
    "moviegenre",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id", ondelete="CASCADE"), primary_key=True),
    Column("genre_id", ForeignKey("genre.id", ondelete="CASCADE"), primary_key=True),
)

movie_actor = Table(
    "movieactor",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id", ondelete="CASCADE"), primary_key=True),
    Column("actor_id", ForeignKey("actor.id", ondelete="CASCADE"), primary_key=True),
)

movie_director = Table(
    "moviedirector",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id", ondelete="CASCADE"), primary_key=True),
    Column("director_id", ForeignKey("director.id", ondelete="CASCADE"), primary_key=True),
)

movie_country = Table(
    "moviecountry",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id", ondelete="CASCADE"), primary_key=True),
    Column("country_id", ForeignKey("country.id", ondelete="CASCADE"), primary_key=True),
)


class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    original_title: Mapped[str] = mapped_column(String(64), index=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    release_date: Mapped[Optional[date]] = mapped_column(Date)
    runtime: Mapped[Optional[int]] = mapped_column(SmallInteger)
    age_rating: Mapped[int] = mapped_column(SmallInteger)
    deniska_rating: Mapped[int] = mapped_column(SmallInteger)
    is_seria: Mapped[bool] = mapped_column(Boolean)

    poster_url: Mapped[Optional[str]] = mapped_column(Text)
    background_poster: Mapped[Optional[str]] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    genres: Mapped[list[Genre]] = relationship(
        secondary=movie_genre,
        back_populates="movies",
        lazy="selectin",
    )

    actors: Mapped[list[Actor]] = relationship(
        secondary=movie_actor,
        back_populates="movies",
        lazy="selectin",
    )

    directors: Mapped[list[Director]] = relationship(
        secondary=movie_director,
        back_populates="movies",
        lazy="selectin",
    )

    countries: Mapped[list[Country]] = relationship(
        secondary=movie_country,
        back_populates="movies",
        lazy="selectin",
    )

    roles: Mapped[list[Role]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    dubbing: Mapped[list[Dubbing]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan",
        lazy="selectin",
    )


class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, index=True)

    movies: Mapped[list[Movie]] = relationship(
        secondary=movie_genre,
        back_populates="genres",
        lazy="selectin",
    )


class Actor(Base):
    __tablename__ = "actor"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    true_name: Mapped[str] = mapped_column(String(64), index=True)
    birth_date: Mapped[Optional[date]] = mapped_column(Date, index=True)
    photo_url: Mapped[Optional[str]] = mapped_column(Text)
    is_female: Mapped[bool] = mapped_column(Boolean, index=True)

    movies: Mapped[list[Movie]] = relationship(
        secondary=movie_actor,
        back_populates="actors",
        lazy="selectin",
    )

    roles: Mapped[list[Role]] = relationship(
        back_populates="actor",
        cascade="all, delete-orphan",
        lazy="selectin",
    )


class Director(Base):
    __tablename__ = "director"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    true_name: Mapped[str] = mapped_column(String(64), index=True)
    birth_date: Mapped[Optional[date]] = mapped_column(Date, index=True)
    photo_url: Mapped[Optional[str]] = mapped_column(Text)
    is_female: Mapped[bool] = mapped_column(Boolean)

    movies: Mapped[list[Movie]] = relationship(
        secondary=movie_director,
        back_populates="directors",
        lazy="selectin",
    )


class Country(Base):
    __tablename__ = "country"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, index=True)

    movies: Mapped[list[Movie]] = relationship(
        secondary=movie_country,
        back_populates="countries",
        lazy="selectin",
    )


class Role(Base):
    __tablename__ = "role"

    __table_args__ = (
        UniqueConstraint(
            "movie_id",
            "actor_id",
            "role_name",
            name="uq_role_movie_actor_name",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id", ondelete="CASCADE"),
        index=True,
    )

    actor_id: Mapped[int] = mapped_column(
        ForeignKey("actor.id", ondelete="CASCADE"),
        index=True,
    )

    role_name: Mapped[str] = mapped_column(String(64))

    movie: Mapped[Movie] = relationship(back_populates="roles")
    actor: Mapped[Actor] = relationship(back_populates="roles")


class Dubbing(Base):
    __tablename__ = "dubbing"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id", ondelete="CASCADE"),
        index=True,
    )

    name: Mapped[str] = mapped_column(String(64))
    dubble_lang: Mapped[str] = mapped_column(String(8), index=True)
    movie_url: Mapped[Optional[str]] = mapped_column(Text)

    movie: Mapped[Movie] = relationship(back_populates="dubbing")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    username: Mapped[str] = mapped_column(
        String(526),
        index=True,
    )

    role: Mapped[str] = mapped_column(
        Text,
        server_default=text("'guest'"),
        default="guest",
    )

    email: Mapped[Optional[str]] = mapped_column(
        String(254),
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(Text)

    birth_date: Mapped[Optional[date]] = mapped_column(Date)
    profile_img: Mapped[Optional[str]] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )