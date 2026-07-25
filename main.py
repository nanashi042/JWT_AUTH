from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import psycopg
from pydantic import BaseModel
from typing import Optional, List


## Database
DATABASE_URL = "postgresql+psycopg://nanashi:Nanashi0210@localhost:5432/learn"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

## DB Model

class User(Base):
    __tablename__ = "users"
    id =Column(Integer, primary_key= True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    roll = Column(String(100), nullable=False)


Base.metadata.create_all(engine)

## Pydantic Model

class UserCreate(BaseModel):
    name:str
    email:str
    roll:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str
    roll:str

    class Config:

        from_attributes = True


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

get_db()




app = FastAPI(title="SQLAlchemy API")


@app.get("/")
def home():
    return {"message": "welcome to api "
            }


@app.get("/users/{user_id}" ,response_model=UserResponse)
def get_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail=" USER MAR GAYA")

    else:
        return user

@app.post("/users/",response_model=UserResponse)
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    if db.query(User).filter(User.email==user.email).first():
        raise HTTPException(status_code=409, detail=" USER ALREADY EXIST" )
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

