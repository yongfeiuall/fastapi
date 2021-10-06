# 导入 FastAPI
from fastapi import FastAPI, Query, Path, Header, Form, UploadFile, Depends, Request
from fastapi import HTTPException, Header
from enum import Enum
from typing import Optional, List

from models.database import SessionLocal, Base, engine

# Base.metadata.create_all(bind=engine) #数据库初始化，如果没有库或者表，会自动创建
#
# # 实例化 FastAPI
# app = FastAPI()

# 创建一个路径
'''
@app.post()
@app.put()
@app.delete()
'''
# @app.get('/')
# # 路径对应操作
# def root():
#     return {'msg': 'hello world!'}

# @app.get('/users/{id}')
# def root(id):
#     return {'name': id}

##############################################3
# @app.get('/users/{id}')
# def root(id: int):
#     return {'user_id': id}
#
# @app.get('/users/zhangsan')
# def root():
#     return {'name': 'zhangsan'}

##############################################3
# class UserName(str, Enum):
#     n1 = 'zhangsan'
#     n2 = 'lisi'
#
# @app.get('/users/{name}')
# def root(name: UserName):
#     if name == UserName.n1:
#         return {'name': name}
#     if name.value == 'lisi':
#         return {'name': name}

##############################################3
# users = [{'name': 'zhangsan'}, {'name': 'lisi'}, {'name': 'wangwu'}]

# @app.get('/users/')
# def root(start: int, limit: int = 2):
#     return users[start : limit]

# @app.get('/users/')
# def root(start: int = 0, limit: int = 2):
#     return users[start : limit]

# books = [{'name': 'python'}, {'name': 'fastapi'}, {'name': 'java'}, ]

# @app.get('/users/{id}')
# def root(id: int = Path(..., gt=12),
#          start: int = 0,
#          limit: Optional[int] = None):
#     if limit:
#         return {id: books[start : limit]}
#     return {id: books[start: ]}

# @app.get('/users/{id}')
# def root(*, id: int = Path(..., gt=12),
#          start: int = 0,
#          limit: Optional[int] = None):
#     if limit:
#         return {id: books[start : limit]}
#     return {id: books[start: ]}

##############################################3
# books = ['python', 'fastapi']
# books = [{'name': 'python'}, {'name': 'fastapi'}, {'name': 'java'}]
# @app.get('/books/')
# def root(book: Optional[str] = Query('Java Script', min_length=2, regex='^J')):
#
#     if book:
#         books.append({'name': book})
#     return books

# @app.get('/books/')
# def root(book: str = Query(..., min_length=2, regex='^J', title='haha', description='Get book detail')):
#
#     if book:
#         books.append({'name': book})
#     return books

# @app.get('/books/')
# def root(book: Optional[list] = Query(None)):
#
#     if book:
#         books.extend(book)
#     return books

##############################################3

# class Book(BaseModel):
#     name: str
#     price: float
#     description: Optional[str] = None
#
# class Author(BaseModel):
#     name: str
#     address: Optional[str] = None
#
# app = FastAPI()
#
# @app.post('/authors/{id}')
# def root(*,
#          id: int = Path(..., gt=12),
#          author: Author,
#          book: Book,
#          publisher: str = Body(...),
#          query: Optional[str] = Query(None)):
#     return id, author, book, publisher, query

# class Book(BaseModel):
#     name: str = Field(..., min_length=2, max_length=10)
#     price: float
#     description: Optional[str] = None
#     tag: List[str] = None
#
# app = FastAPI()
#
# @app.post('/books/')
# def root(book: Book = Body(..., embed=True),
#          query: Optional[str] = None):
#     return book, query


# class Author(BaseModel):
#     name: str
#     address: Optional[str] = None
#
#
# class Book(BaseModel):
#     name: str
#     price: float
#     description: Optional[str] = None
#     author: Author
#
# app = FastAPI()
#
# @app.post('/authors/{id}')
# def root(*,
#          id: int = Path(..., gt=12),
#          book: Book):
#     return id, book

##############################################3

# @app.get('/users/')
# def root(user_agent: Optional[str] = Header(None),
#          sid: Optional[str] = Cookie(None)):
#     print(sid)
#     return {'User-Agent': user_agent}, {'ck': sid}

# @app.get('/users/')
# def root(user_agent: Optional[str] = Header(None),
#          sid: Optional[str] = Cookie(None)):
#     return {'User-Agent': user_agent}, {'sid': sid}

##############################################3
# @app.post('/login/')
# def root(username : str = Form(...), password: str = Form(...)):
#     return {'username': username, 'password': password}

# @app.post('/upload/')
# def root(file: UploadFile = File(...)):
#     return {'filename': file.filename}
#
# @app.post('/uploads/', status_code=status.HTTP_200_OK)
# def root(files: List[UploadFile] = File(...)):
#     return {'filename': [file.filename for file in files]}

##############################################3

# class User(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     adress: Optional[str] = 'beijing'
#
# class UserRes(BaseModel):
#     username: str
#     email: EmailStr
#     address: Optional[str] = 'beijing'
#
# @app.post('/user/register/', response_model=UserRes, response_model_exclude_unset=True)
# def register(user: User):
#     return user

##############################################3

# def result(start: int = 0, limit: int = 10):
#     return {'start': start, 'limit': limit}
#
# @app.get('/users/')
# def users(res: dict = Depends(result)):
#     return res
#
# @app.get('/books/')
# def books(res: dict = Depends(result)):
#     return res

# class Result():
#     def __init__(self, start: int = 0, limit: int = 10):
#         self.start = start
#         self.limit = limit
#
# @app.get('/users/')
# def users(res: Result = Depends()):
#     return res

# def result1(start: int = 0):
#     return start
#
# def result2(start: int = Depends(result1), limit: int = 0):
#     if limit:
#         return limit
#     return start
#
# @app.get('/users/')
# def users(res: dict = Depends(result2)):
#     return res

# def result1(start: int):
#     if start != 2:
#         raise HTTPException(status_code=400, detail='start not == 2')
#
# def result2(limit: int):
#     if limit != 5:
#         raise HTTPException(status_code=400, detail='limit not == 5')
#
# app = FastAPI(dependencies=[Depends(result1), Depends(result2)])
#
# @app.get('/users/')
# def users():
#     return {'status': 'ok'}
#
# @app.get('/books/')
# def users():
#     return {'status': 'ok'}

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
# @app.get('/users/')
# def users(token: str = Depends(oauth2_scheme)):
#     return {'token': token}

# fake_user = {
#     'admin':{
#         'username': 'admin',
#         'hash_password': 'fakehashadmin',
#         'enabled': True
#     }
# }
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
# def fake_hash_password(password: str):
#     return "fakehash" + password
#
# class User(BaseModel):
#     username: str
#     enbaled: Optional[bool] = None
#
# class UserPwd(User):
#     hash_password: str
#
#
# @app.post('/login')
# def login(form: OAuth2PasswordRequestForm = Depends()):
#     user = fake_user.get(form.username)
#     if not user:
#         raise HTTPException(status_code=400, detail='user incorrect')
#     u = UserPwd(**user)
#     hashpwd = fake_hash_password(form.password)
#     if hashpwd != u.hash_password:
#         raise HTTPException(status_code=400, detail='passwod incorrect')
#
#     return {"access_token": u.username, "token_type": "bearer"}

##############################################3


# Dependency


# Dependency
# def get_db():
#     """
#     每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
#     :return:
#     """
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# # 新建用户
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, models: Session = Depends(get_db)):
#     return crud.create_user(models=models, user=user)
#
#
# # 通过id查询用户
# @app.get("/user/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, models: Session = Depends(get_db)):
#     db_user = crud.get_user(models, user_id=user_id)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# # 所有用户
# @app.get('/users/', response_model=List[schemas.User])
# def read_users(start: int=0, limit: int=10, models: Session = Depends(get_db)):
#     return crud.get_users(models, start, limit)
#
# # Delete user
# @app.delete('/user/{user_id}', response_model=schemas.User)
# def delete_user(user_id: int, models: Session = Depends(get_db)):
#     db_user = crud.delete_user(models, user_id=user_id)
#     if not db_user:
#         raise HTTPException(status_code=400, detail='User not found')
#     return db_user
#
# # Update User
# @app.put('/user/{user_id}', response_model=schemas.User)
# def update_user(user_id: int, update_user: schemas.UserUpdate, models: Session = Depends(get_db)):
#     db_user = crud.update_user(models, user_id=user_id, update_user=update_user)
#     if not db_user:
#         raise HTTPException(status_code=400, detail='User not found')
#     return db_user

##############################################3
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
#
# app.mount("/static", StaticFiles(directory="static"), name="static")
#
# templates = Jinja2Templates(directory="templates")
#
# # Return html page
# @app.get("/user/{user_id}", response_class=HTMLResponse)
# def read_user(request: Request, user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return templates.TemplateResponse('index.html', {'request': request, 'username': db_user.email})

##############################################3
from jose import jwt
from datetime import datetime, timedelta

# 加密密钥
SECRET_KEY = "testjwt"

# 设置过期时间 示例5分钟
expire = datetime.utcnow() + timedelta(minutes=5)

# exp 是固定写法必须得传  username和uid是自己存的值
to_encode = {"exp": expire, "username": "admin", "uid": "12345"}

# 生成token
token = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

print(token)

from jose.exceptions import ExpiredSignatureError, JWTError
try:
    payload = jwt.decode(token, SECRET_KEY, algorithms="HS256" )
    print(payload)
except ExpiredSignatureError as e:
    print("token过期")
except JWTError as e:
    print("token验证失败")
