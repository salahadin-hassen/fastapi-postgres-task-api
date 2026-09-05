from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    completed: bool

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
@app.get("/health")
def read_health():
    return {"Health": "good"}

@app.post("/tasks")

def create_tasks(task: Task):
    task_title = task.title
    task_description = task.description
    task_completed = task.completed
    return {"status": "success",
            "message": f"Task {task_title} was created."}
@app.get("/tasks")

def read_tasks():
    return []

