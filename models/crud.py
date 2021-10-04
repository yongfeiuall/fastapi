from sqlalchemy.orm import Session
from . import models, schemas


# Get user by id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get user by mail
def get_user_by_mail(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Get all users
def get_users(db: Session, start: int=0, limit: int=10):
    return db.query(models.User).offset(start).limit(limit).all()

# creae user
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    user = models.User(email=user.email, hash_password=fake_hashed_password)
    db.add(user)
    db.commit()  # 提交保存到数据库中
    db.refresh(user)  # 刷新
    return user

# Delete user
def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        db.flush()
        return user


# Update user
def update_user(db: Session, user_id: int, update_user: schemas.UserUpdate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        update_user = update_user.dict(exclude_unset=True)
        for k, v in update_user.items():
            setattr(user, k, v)
        db.commit()
        db.flush()
        db.refresh(user)
        return user