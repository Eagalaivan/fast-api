from fastapi import Depends,FastAPI
from sqlalchemy.orm import Session
from .database import SessionLocal,engine
from .models import *
from pydantic import BaseModel
import random
from uuid import UUID
app=FastAPI()

Base.metadata.create_all(bind=engine)
class JobModel(BaseModel):
    id: int
    job_description: str
    is_active: bool
class CandidateModel(BaseModel):
    c_id: int
    c_name: str
    c_degree: str
class role(BaseModel):
    role_name:str

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
    del_id =id
    res = db.execute("DELETE FROM jobs WHERE id={}".format(del_id))
    db.commit()
    return {"query passed":"removed"}

@app.get("/job/{id}")
def get_job_byid(id: int, db: Session = Depends(get_db)):
    search_id = id
    res=db.execute("SELECT job_description FROM jobs WHERE id = {}".format(search_id)) 
    result=res.fetchall()
    db.commit()
    return {"query passed":result}
@app.post("/job/{id}/apply")
def apply_job_by_id(role: role,id: int, candidatesvalidation: CandidateModel,db: Session = Depends(get_db)):
    apply_id = id
    role.role_name=role.role_name
    candidatesvalidation.c_name  =candidatesvalidation.c_name
    candidatesvalidation.c_id=candidatesvalidation.c_id
    candidatesvalidation.c_degree=candidatesvalidation.c_degree
    application_id = random.randint(100,657)
    res = db.execute("INSERT INTO jobapplication (job_application_id,j_id,c_name,j_role) values ({},{},'{}','{}')".format(application_id,candidatesvalidation.c_id,candidatesvalidation.c_name,role.role_name))
    db.commit()
    return {"query":"inserted"}