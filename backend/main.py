import os

from fastapi import FastAPI

from config import config
from apps.images_api.routers import router as images_api_router


app = FastAPI(
    debug=config.DEBUG,
    version=os.getenv("VERSION", 'blabla'),
)

app.include_router(images_api_router)
