from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.user import UserDB
from app.schemas.user import UserCreate, TokenOut
from app.utils.security import verify_password, create_access_token
from app.crud.user import get_user_by_username

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)

@router.post("/login", response_model=TokenOut)
async def login(payload: UserCreate, response: Response,db: AsyncSession = Depends(get_db)):
    user = await get_user_by_username(db, payload.username)

    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="bad credentials")

    token = create_access_token(subject=user.id, extra_clims={"role": user.role})
    response.set_cookie(
        "access_token", token,
        httponly=True, path="/", max_age=60*60
    )
    return {"access_token": token, "token_type": "bearer"}
