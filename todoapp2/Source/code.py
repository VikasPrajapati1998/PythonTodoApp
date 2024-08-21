from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from uuid import uuid4, UUID
import json

# =================================================================================================================================
class ToDoItem(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# ==================================================================================================================================

# In-memory database simulation
db = []

app = FastAPI()

# Home
@app.get("/")
async def home():
    return "Welcome to todo."

# POST
@app.post("/todos/", response_model=list[dict])
async def create_todo(todo: ToDoItem):
    with open("data.json", "r+") as file:
        db = json.load(file)
    
    todo_id = str(uuid4())
    data = {"id": todo_id, "title": todo.title, "description": todo.description, "completed": todo.completed}
    db.append(data)
    print("Post db: ", db)
    with open("data.json", 'w+') as file:
        json.dump(db, file, indent=4)
    return db

# GET
@app.get("/todos/", response_model=list[dict])
async def read_todos():
    with open("data.json", "r+") as file:
        db = json.load(file)
    print("Get db: ", db)
    return db

# GET By Id
@app.get("/todos/{todo_id}", response_model=list[dict])
async def read_todo(todo_id: UUID):
    with open("data.json", "r+") as file:
        db = json.load(file)
    
    data = [ele for ele in db if ele["id"] == str(todo_id)]
    if not data:
        raise HTTPException(status_code=404, detail="ToDo not found")
    print("Get by Id : ", data)
    return data

# PUT : Update
@app.put("/todos/{todo_id}", response_model=list[dict])
async def update_todo(todo_id: UUID, todo: ToDoItem):
    with open("data.json", "r+") as file:
        db = json.load(file)
    data = [ele for ele in db if ele["id"] == str(todo_id)]
    if not data:
        raise HTTPException(status_code=404, detail="ToDo not found")
    
    new_data = {"title": todo.title, "description": todo.description, "completed": todo.completed}
    for ele in db:
        if ele['id'] == str(todo_id):
            ele['title'] = new_data["title"]
            ele['description'] = new_data["description"]
            ele['completed'] = new_data['completed']
            
    print("Updated db : ", db)
    with open("data.json", 'w+') as file:
        json.dump(db, file, indent=4)
    return db

# DELETE
@app.delete("/todos/{todo_id}", response_model=list[dict])
async def delete_todo(todo_id: UUID):
    with open("data.json", "r+") as file:
        db = json.load(file)
    
    data = [ele for ele in db if ele["id"] == str(todo_id)]
    if not data:
        raise HTTPException(status_code=404, detail="ToDo not found")
    
    for i, dct in enumerate(db):
        if dct['id'] == str(todo_id):
            item = db.pop(i)
    print("Deleted Item : ", item)
    
    with open("data.json", 'w+') as file:
        json.dump(db, file, indent=4)
    return db
