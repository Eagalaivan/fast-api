from typing import Optional

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"hello : world"}
@app.get("/stuff/{stuff_id}")
def read_stuff(stuff_id:    int, query:Optional[str]=None):
    return {"stuff_id":stuff_id,"query":query}
@app.get("/jobs")
def jobs_list():
    return {"Jobs listings : content"}
