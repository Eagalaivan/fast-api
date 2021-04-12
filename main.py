from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def index():
    return {"index page":"Content"}

@app.get("/jobs/{id}")
def show_jobs(id: int):
    return {"id":id}
@app.post("/jobs/{id}")
def create_job(id:int):
     return {"id":id}

@app.delete("/jobs/{id}")
def delete_job(id:int):
     return {"id":id}