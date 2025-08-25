from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (React Vite default port 5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Task Model
class Task(BaseModel):
    title: str
    completed: bool = False

tasks = []
task_id_counter = 1

# Create
@app.post("/tasks")
def create_task(task: Task):
    global task_id_counter
    new_task = {"id": task_id_counter, "title": task.title, "completed": task.completed}
    tasks.append(new_task)
    task_id_counter += 1
    return new_task

# Read
@app.get("/tasks")
def get_tasks():
    return tasks

# Update
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = updated_task.title
            t["completed"] = updated_task.completed
            return t
    return {"error": "Task not found"}

# Delete
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": "Task deleted"}

# Root check
@app.get("/")
def root():
    return {"status": "Backend is running!"}


# Root check
@app.get("/")
def root():
    return {"activeStatus": True, "error": False}


