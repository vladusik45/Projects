from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import app.models, app.schemas as schemas, app.crud
from app.database import engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return app.crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.UserRead])
def read_users(db: Session = Depends(get_db)):
    return app.crud.get_users(db)

@app.post("/posts/", response_model=schemas.PostRead)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return app.crud.create_post(db, post)

@app.get("/posts/", response_model=list[schemas.PostRead])
def read_posts(db: Session = Depends(get_db)):
    return app.crud.get_posts(db)
