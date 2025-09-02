from pydantic import BaseModel, Field
from datetime import date, datetime
# from typing import Optional
from typing import List

class UserBase(BaseModel):
    id: int
    username: str
    role: str
    email: str | None = None
    # password_hash: str
    birth_date: date | None = None
    profile_img: str | None = None
    # created_at: datetime = Field(..., description="UTC timestamp")

class UserDB(UserBase):
    """Вся інфа з юзера з ПАРОЛЕМ"""
    password_hash: str
    created_at: datetime = Field(..., description="UTC timestamp")

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    """для реєстрації"""
    username: str
    password: str

class UserOut(UserBase):
    """
    для показу юзера (без пароля)
    from_attributes = True
    """
    class Config:
        from_attributes = True
