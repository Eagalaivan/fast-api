from fastapi import Depends, FastAPI, Request, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import *
from pydantic import BaseModel
import random
from uuid import UUID
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.mount("/assets", StaticFiles(directory="fast-api/templates"), name="assets")
Base.metadata.create_all(bind=engine)


class JobModel(BaseModel):
    id: str
    job_description: str
    is_active: bool

class delete_id():
    id:str

class CandidateModel(BaseModel):
   
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

@app.get("/home")
def home(request:Request):
   
    return templates.TemplateResponse("index.html", {
        "request": request
    })
@app.get("/")
def index(request: Request):
     return templates.TemplateResponse("homepage.html", {
        "request": request
    })


@app.get("/jobs/")
def show_jobs(request: Request, db: Session = Depends(get_db)):
    res = db.execute("SELECT * FROM jobs")
    result = res.fetchall()
    db.commit()
   
    return templates.TemplateResponse("jobs.html", context={
        "request": request,
        "res":result,
        "var":2

    })


@app.post("/jobs/")
def create_job(request:Request ,val: JobModel, db: Session = Depends(get_db)):
    id = val.id
    print(id)
    job_description = val.job_description
    is_active = val.is_active
    db.execute("INSERT INTO jobs (id,job_description,is_active) values ({},'{}',{})".format(
        id, job_description, is_active))
    db.commit()
    return templates.TemplateResponse("jobs.html", context={
        "request": request     

    })



@app.delete("/jobs/{id}")
def delete_job(request:Request, id: str, db: Session = Depends(get_db)):
    del_id = id
    db.execute("DELETE FROM jobs WHERE id={}".format(del_id))
    db.commit()
    return templates.TemplateResponse("jobs.html", context={
        "request": request     

    })


@app.get("/job/{id}")
def get_job_byid(request:Request,id: int, db: Session = Depends(get_db)):
    search_id = id
 
    res = db.execute(
        "SELECT * FROM jobs WHERE id = {}".format(search_id))
    result = res.fetchall()
    db.commit()
    
    return templates.TemplateResponse("views.html", context={
        "request": request,
        "result":result,
        

    })


@app.post("/job/{jid}/apply")
def apply_job_by_id(jid:str,request: Request,candidatesvalidation: CandidateModel, db: Session = Depends(get_db)):
    candidatesvalidation.role_name = candidatesvalidation.role_name
    candidatesvalidation.c_name = candidatesvalidation.c_name
    candidatesvalidation.c_degree = candidatesvalidation.c_degree
    application_id = random.randint(100, 657)
    res = db.execute("INSERT INTO jobapplication (job_application_id,j_id,c_name,j_role) values ({},{},'{}','{}')".format(
        application_id, jid, candidatesvalidation.c_name, candidatesvalidation.role_name))
        
    db.commit()
    res2= db.execute("SELECT * FROM jobapplication")
    result2 =res2.fetchall()
    db.commit()

    return templates.TemplateResponse("views.html", context={
        "request": request,
        "res":result2
        

    })


