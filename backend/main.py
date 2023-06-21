from fastapi import FastAPI

from config import config
from apps.images_api.routers import router as images_api_router


app = FastAPI(
    debug=config.DEBUG,
    version=config.VERSION,
)

app.include_router(images_api_router)
