from fastapi import Depends,FastAPI
from sqlalchemy.orm import Session
from .database import SessionLocal,engine
from .models import *
from pydantic import BaseModel

app=FastAPI()

Base.metadata.create_all(bind=engine)
class JobModel(BaseModel):
    id: int
    job_description: str
    is_active: bool
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
    db.commit()
    return {"query passed":result}

@app.post("/jobs/")
def create_job(val:JobModel,db: Session = Depends(get_db)):
    id =val.id
    job_description =val.job_description
    is_active = val.is_active
    db.execute("INSERT INTO jobs (id,job_description,is_active) values ({},'{}',{})".format(id,job_description,is_active))
    db.commit()
    return {"query passed": "added"}

@app.delete("/jobs/")
def delete_job(id:int,db: Session = Depends(get_db)):
    del_id=id
    res=db.execute("DELETE FROM jobs WHERE id={}".format(del_id))
    try:
        if(res.fetchall()):
           pass
    finally:
         return {"no records found with id":del_id}
    db.commit()

    return {"query passed":"removed"}



     