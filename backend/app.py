from fastapi import FastAPI

from config import config
from routers import routers


app = FastAPI(
    debug=config.DEBUG,
    version=config.VERSION,
)

app.include_router(routers.router, prefix='/sd', tags=['Stable Diffusion'])
