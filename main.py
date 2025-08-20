from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()



class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


tasks = []

# Create
@app.post('/tasks')

def create_task(task: Task):
    tasks.append(task)
    return task

# Read
@app.get('/tasks')

def get_tasks():
    return tasks

# Update
@app.put("/tasks/{task_id}")

def update_task(task_id: int, updated_task: Task):
    for t in tasks:
        if t.id == task_id:
            t.title = updated_task.title
            t.completed = updated_task.completed
            return t
    return {"error": "Task not found"}

# Delete
@app.delete("/tasks/{task_id}")

def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": "Task deleted"}

@app.get('/')

def root():
    return {
        "activeStatus": True,
        "error": False
    }

