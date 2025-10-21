from fastapi import FastAPI

# Load environment variables from .env file
from src.routes import base, data

app = FastAPI()
#funtion control what in and out from this function @
app.include_router(base.base_router, prefix="/base")
app.include_router(data.data_router, prefix="/data")