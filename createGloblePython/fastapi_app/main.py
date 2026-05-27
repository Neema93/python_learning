from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
#fackdatabase
tasks = []
class Task(BaseModel): 
    title: str
    completed: bool = False
# home get method
@app.get("/")
def home():
    return{"message":"Fastapi is running"}
#get all task
@app.get("/tasks")
def get_tasks():
    return tasks

#get task by id
@app.get("/tasks/{task_id}")
def get_taskid(task_id:int):
       
    if task_id < len(tasks):
        return tasks[task_id]

    return {"error": "Task not found"}
# add task
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
#delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)

        return {
            "message": "Task deleted successfully",
            "deleted_task": removed_task
        }

    return {"error": "Task not found"}