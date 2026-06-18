from sys import prefix

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.user import UserDB
from app.schemas.user import UserCreate, TokenOut, UserOut, UserRegister
from app.utils.security import verify_password, create_access_token
from app.crud.user import get_user_by_username
from app.crud.user import reg_user
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    tags=["auth"]
)

@router.post("/login", response_model=TokenOut)
async def login(payload: UserCreate, response: Response,db: AsyncSession = Depends(get_db)):
    user = await get_user_by_username(db, payload.username)

    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail='bad credentials')

    token = create_access_token(subject=user.id, extra_clims={"role": user.role})
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax",
        domain='.deniskafilms.com',
        path="/",
        max_age=60*60*24*7 #7 діб в секундах
    )
    return {"access_token": token, "token_type": "bearer"}

#уже є такий самий роут але GET
@router.post("/register", response_model=UserOut)
#треба буде доробити і видавати токен після реєстрації
async def register_user(payload: UserRegister, db: AsyncSession = Depends(get_db)):
    try:
        user = await reg_user(db, payload)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="login or username already exists")
    return user