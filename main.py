from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import engine, SessionLocal
from models import Base, Task
class TaskCreate(BaseModel):
    title: str              
    description: str  
    completed: bool

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
       yield db
    finally:
        db.close()
 

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
@app.get("/health")
def read_health():
    return {"Health": "good"}

@app.post("/tasks")

def create_tasks(task: TaskCreate, db = Depends(get_db)):
       db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed
    )
       db.add(db_task)
       db.commit()
       return {"status": "success"}

@app.get("/tasks")

def read_tasks():
    return []

