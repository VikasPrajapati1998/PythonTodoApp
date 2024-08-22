from fastapi import APIRouter, Request
import json
from app.apis.package.temp import get_hello_from_country

router = APIRouter()

@router.post("/hello")
async def hello_world(request: Request):
    try:
        request_body = await request.body()
        input_data = json.loads(request_body.decode('utf-8')).get('data', {})
        
        response = get_hello_from_country(input_data)
        return {"message": response}
    except Exception as e:
        print("routers.package.temp error:", e)
        return {"error": "An error occurred"}


