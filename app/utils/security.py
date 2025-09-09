from passlib.context import CryptContext
from typing import Optional, Dict, Any
from datetime import datetime, date, timezone, timedelta

from jose import jwt

pwd_ctx = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12,
)

SECRET_KEY = "JWT_SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(passwort: str) -> str:
    """Хешує пароль (сіль генерується автоматично, все всередині рядка)."""
    return pwd_ctx.hash(passwort)

def verify_password(password: str, stored_hash: str) -> bool:
    """Поровіряє пароль з хешом і вертає True чи False"""
    return pwd_ctx.verify(password, stored_hash)

def create_access_token(subject: str | int,
                        extra_clims: Optional[Dict[str, Any]] = None,
                        expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES
                        ) -> str:
    now = datetime.now(timezone.utc)
    to_encode: Dict[str, Any] = {"sub": str(subject), "iat": int(now.timestamp())} #тут базову схему для пейлоад для кодування
    if extra_clims:
        to_encode.update(extra_clims)
    expire = now + timedelta(minutes=expires_minutes)
    to_encode["exp"] = int(expire.timestamp())
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def check_player(token) -> bool:
    """
    повертає тру чи фолс у залежності від JWT токена
    """
    if not token:
        return False
    # тут маэ бути код !!!!!!!
    ...
