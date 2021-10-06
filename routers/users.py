from fastapi import APIRouter, Depends, HTTPException, Request, status, Header, Form, Cookie
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi.templating import Jinja2Templates
import functools
from models import crud,schemas
from dependencies import get_db
from utils import jwttoken

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# 新建用户
@router.post("/register/", response_model=schemas.User, tags=['users'])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)


# 通过id查询用户
@router.get("/user/{user_id}", response_model=schemas.User, tags=['users'])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# 所有用户
@router.get('/users/', response_model=List[schemas.User], tags=['users'])
def read_users(start: int=0, limit: int=10, db: Session = Depends(get_db)):
    return crud.get_users(db, start, limit)


# Delete user
@router.delete('/user/{user_id}', response_model=schemas.User, tags=['users'])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail='User not found')
    return db_user


# Update User
@router.put('/user/{user_id}', response_model=schemas.User, tags=['users'])
def update_user(user_id: int, update_user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id=user_id, update_user=update_user)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return db_user


@router.post('/api/login', tags=['users'])
def user_login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_mail(db, username)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if password != db_user.hash_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='passwod incorrect')

    data = {'email': db_user.email, 'user_id': db_user.id}
    token = jwttoken.create_jwt_token(data)

    return {"token": token}

@router.get('/current/user', tags=['users'])
def get_current_user(token: Optional[str] = Header(...), db: Session = Depends(get_db)):
    payload = jwttoken.decode_jwt_token(token)
    email: str = payload.get("email")

    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'access token failed',
                            # 根据OAuth2规范, 认证失败需要在响应头中添加如下键值对
                            headers={'WWW-Authenticate': "Bearer"}
                            )

    user = crud.get_user_by_mail(db, email=email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#################################################################################

# # User login
# @router.get('/login', response_class=HTMLResponse)
# def login_page(request: Request):
#     return templates.TemplateResponse('login.html', {'request': request})
#
# @router.get('/index', response_class=HTMLResponse)
# def home(request: Request):
#     return templates.TemplateResponse('index.html', {'request': request})
#
# @router.post('/api/login', tags=['users'], response_class=HTMLResponse)
# def user_login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_mail(db, username)
#     if not db_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     if password != db_user.hash_password:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='passwod incorrect')
#
#     data = {'email': db_user.email, 'user_id': db_user.id}
#     token = jwttoken.create_jwt_token(data)
#     res = JSONResponse({"token": token})
#     res.set_cookie(key='token', value=token)
#     res.set_cookie(key='email', value=db_user.email)
#
#     # return RedirectResponse('/index', status_code=status.HTTP_302_FOUND)
#     # return templates.TemplateResponse('index.html', {'request': request, 'username': db_user.email})
#     return res
#
# @router.get('/ck')
# def get_cookie(token: Optional[str] = Cookie(None)):
#     return {'token': token}