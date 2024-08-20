from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from uuid import uuid4, UUID

# Define the ToDo model
class ToDoItem(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory database simulation
db = {}

app = FastAPI()

# POST
@app.post("/todos/", response_model=ToDoItem)
async def create_todo(todo: ToDoItem):
    todo_id = str(uuid4())
    db[todo_id] = todo
    return {**todo.dict(), "id": todo_id}

# GET
@app.get("/todos/", response_model=List[ToDoItem])
async def read_todos():
    return [item for item in db.values()]

# GET By Id
@app.get("/todos/{todo_id}", response_model=ToDoItem)
async def read_todo(todo_id: UUID):
    todo = db.get(str(todo_id))
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

# PUT : Update
@app.put("/todos/{todo_id}", response_model=ToDoItem)
async def update_todo(todo_id: UUID, todo: ToDoItem):
    if str(todo_id) not in db:
        raise HTTPException(status_code=404, detail="ToDo not found")
    db[str(todo_id)] = todo
    return todo

# DELETE
@app.delete("/todos/{todo_id}", response_model=ToDoItem)
async def delete_todo(todo_id: UUID):
    todo = db.pop(str(todo_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo
