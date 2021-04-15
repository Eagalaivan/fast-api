from fastapi import Depends, FastAPI, Request, BackgroundTasks
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import *
from pydantic import BaseModel
import random
from uuid import UUID
from fastapi.templating import Jinja2Templates

app = FastAPI()

Base.metadata.create_all(bind=engine)


class JobModel(BaseModel):
    id: str
    job_description: str
    is_active: bool


class CandidateModel(BaseModel):
    c_id: str
    c_name: str
    c_degree: str
    role_name: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory="fast-api/templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request

    })


@app.get("/jobs/")
def show_jobs(request: Request, db: Session = Depends(get_db)):
    res = db.execute("SELECT * FROM jobs")
    result = res.fetchall()
    db.commit()
    return {"json": result}
    # return templates.TemplateResponse("jobs.html",{"request":request})


@app.post("/jobs/")
def create_job(val: JobModel, db: Session = Depends(get_db)):
    id = val.id
    job_description = val.job_description
    is_active = val.is_active
    db.execute("INSERT INTO jobs (id,job_description,is_active) values ({},'{}',{})".format(
        id, job_description, is_active))
    db.commit()
    return {"query passed": "added"}


@app.delete("/jobs/")
def delete_job(id: str, db: Session = Depends(get_db)):
    del_id = id
    res = db.execute("DELETE FROM jobs WHERE id={}".format(del_id))
    db.commit()
    return {"query passed": "removed"}


@app.get("/job/{id}")
def get_job_byid(id: str, db: Session = Depends(get_db)):
    search_id = id
    res = db.execute(
        "SELECT job_description FROM jobs WHERE id = {}".format(search_id))
    result = res.fetchall()
    db.commit()
    return {"query passed": result}


@app.post("/job/apply/")
def apply_job_by_id(candidatesvalidation: CandidateModel, db: Session = Depends(get_db)):

    candidatesvalidation.role_name = candidatesvalidation.role_name
    candidatesvalidation.c_name = candidatesvalidation.c_name
    candidatesvalidation.c_id = candidatesvalidation.c_id
    candidatesvalidation.c_degree = candidatesvalidation.c_degree
    application_id = random.randint(100, 657)
    res = db.execute("INSERT INTO jobapplication (job_application_id,j_id,c_name,j_role) values ({},{},'{}','{}')".format(
        application_id, candidatesvalidation.c_id, candidatesvalidation.c_name, candidatesvalidation.role_name))
    db.commit()
    return {"query": "inserted"}


@app.get("/ja")
def checl(id: str, s1: str, s2: str, s3: str, s4: str):

    return {id, s1, s2, s3, s4}
