from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
#fackdatabase
tasks = []
class Task(BaseModel): 
    title: str
    completed: bool = False

@app.get("/")
def home():
    return{"message":"Fastapi is running"}

@app.get("/tasks")
def get_tasks():
    return tasks
@app.get("/tasks/{task_id}")
def get_taskid(task_id:int):
       
    if task_id < len(tasks):
        return tasks[task_id]

    return {"error": "Task not found"}

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {
        "message": "Task added",
        "task": task
    }
# Update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    if task_id < len(tasks):
        tasks[task_id] = updated_task

        return {
            "message": "Task updated",
           "updated_task": tasks[task_id]
        }

    return {"error": "Task not found"}