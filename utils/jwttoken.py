from jose import jwt
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, status
import config


def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(claims=to_encode, key=config.SECRET_KEY, algorithm=config.ALGORITHM)
    return token


def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token=token, key=config.SECRET_KEY, algorithms=config.ALGORITHM)
        return payload
    except (jwt.JWTError, jwt.ExpiredSignatureError, AttributeError) as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'access token failed: {e}',
                            # 根据OAuth2规范, 认证失败需要在响应头中添加如下键值对
                            headers={'WWW-Authenticate': "Bearer"}
                            )
