from jose import jwt, JWTError, ExpiredSignatureError
from app.utils.security import hash_password


print(hash_password("ggsgow"))