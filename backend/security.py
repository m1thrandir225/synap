from typing import Any, Optional, Union
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    subject: Union[str, Any], expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a JWT access token

    Parameters:
        subject (Union[str, Any]): The subject for which the token is created
        expires_delta (timedelta, optional): The expiration time for the access
        token.
    """
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}

    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm="HS256")

    return encoded_jwt


def generate_password_hash(raw: str) -> str:
    """
    Generate a password hash using bcrypt
    """
    return pwd_context.hash(raw)


def verify_password(raw: str, hashed: str) -> bool:
    """
    Verify a generated password hash using bcrypt
    """
    return pwd_context.verify(raw, hashed)
