from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
#fackdatabase
tasks = []
class Task(BaseModel): # type: ignore
    title: str
@app.get("/")
def home():
    return{"message":"Fastapi is running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {
        "message": "Task added",
        "task": task
    }