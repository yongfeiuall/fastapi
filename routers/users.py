from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import crud,schemas
from dependencies import get_db

router = APIRouter()


# 新建用户
@router.post("/users/", response_model=schemas.User, tags=['users'])
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
        raise HTTPException(status_code=400, detail='User not found')
    return db_user