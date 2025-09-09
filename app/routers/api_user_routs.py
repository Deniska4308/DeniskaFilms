from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.user import UserDB, UserCreate, UserOut
from app.crud.user import get_user_by_id, post_user
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/api/user",
    tags=["api"]
)

@router.get("/{user_id}", response_model=UserDB)
async def get_user_by_UserId(user_id: int, db: AsyncSession = Depends(get_db)):
    user_data = await get_user_by_id(db, user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found.")
    return user_data

@router.post("/create", response_model=UserOut, tags=["auth"], status_code=201)
async def create_user(payload: UserCreate,db: AsyncSession = Depends(get_db)):
    try:
        user = await post_user(db, payload)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="login or username already exists")
    return user