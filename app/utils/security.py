from passlib.context import CryptContext

pwd_ctx = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12,
)

def hash_password(passwort: str) -> str:
    """Хешує пароль (сіль генерується автоматично, все всередині рядка)."""
    return pwd_ctx.hash(passwort)

def verify_password(password: str, stored_hash: str) -> bool:
    """Поровіряє пароль з хешом і вертає True чи False"""
    return pwd_ctx.verify(password, stored_hash)
