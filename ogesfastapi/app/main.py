from fastapi import FastAPI
from app.routers.package.temp import router as temp_router

app = FastAPI()

# Include routers with their specific prefix
app.include_router(temp_router, prefix="/intro")

@app.get("/")
async def root():
    return "Welcome to FastAPI."


