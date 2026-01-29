from sqlalchemy.orm import Session
import app.models, app.schemas as schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = app.models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(app.models.User).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = app.models.Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session):
    return db.query(app.models.Post).all()
