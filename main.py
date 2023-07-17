from typing import Union

from fastapi import FastAPI,Response
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.base import api_router 
from db.session import engine  
from db.base import Base  
import uvicorn



def include_router(app):
	app.include_router(api_router)


def create_tables():
	Base.metadata.create_all(bind=engine)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	create_tables()
	return app


app = start_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8005, reload=True)

