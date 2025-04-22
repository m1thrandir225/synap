from typing import Any, Optional, Union
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from backend.config import settings
from enum import Enum
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class JWT_TYPE(Enum):
    ACCESS = 1
    REFRESH = 2

def create_jwt_token(
    subject: Union[str, Any],
    type: JWT_TYPE
) -> str:
    """
    Create a JWT access token

    Parameters:
        subject (Union[str, Any]): The subject for which the token is created
        type (JWT_TYPE): The type of jwt token to be generated
    """
    if type == JWT_TYPE.ACCESS:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    elif type == JWT_TYPE.REFRESH:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}

    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

    return encoded_jwt


def decode_token(
    token: str, key: Optional[str] = None, type: Optional[JWT_TYPE] = JWT_TYPE.ACCESS
) -> Optional[str]:
    """
    Decode a JWT Token

    Parameters:
        token (str): The token
        key (str | None, optional): A key to extract from the token. Defaults to
        None.
        type (str, optional): The type of the token [access or refresh].
        Defaults to access

    Return:
        str | None: The extracted data from the token or None if the token is
        invalid
    """
    try:
        if type == JWT_TYPE.REFRESH:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        else:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        if key:
            return payload.get(key)

        return payload.get("sub")
    except JWTError as e:
        print(e)
        return None


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
