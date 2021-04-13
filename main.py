from fastapi import Depends,FastAPI
from sqlalchemy.orm import Session
from .database import SessionLocal,engine
from .models import *
from pydantic import BaseModel

app=FastAPI()

Base.metadata.create_all(bind=engine)
class JobModel(BaseModel):
    id: int

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"index page":"Content"}
@app.get("/jobs/")
def show_jobs( db: Session = Depends(get_db)):
    res=db.execute("SELECT * FROM jobs")
    result=res.fetchall()
    print(result)
    db.commit()
    return {"query passed":result}

@app.post("/jobs/{id}")
def create_job(id:int):
     pass

@app.delete("/jobs/{id}")
def delete_job(id:int):
     pass