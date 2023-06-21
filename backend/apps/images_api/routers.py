from typing import Annotated

from fastapi import APIRouter, Body

from config import config
from .models.data_models import (
    Text2ImgOut,
    FetchOut,
    SystemLoadOut,
    Text2ImgIn,
)
from .services.sd import SDClient


router = APIRouter(prefix='/api/v1/sd', tags=['Stable Diffusion'])


@router.post(
    '/text_to_img',
    response_model=Text2ImgOut,
    response_model_by_alias=False,
)
async def text_to_image(
        params: Annotated[Text2ImgIn, Body()]
):
    ai_client = SDClient(config=config)

    return await ai_client.text_to_image(params)


@router.get(
    '/fetch',
    response_model=FetchOut,
    response_model_by_alias=False,
)
async def fetch_image(img_id: int):
    ai_client = SDClient(config=config)

    resp = await ai_client.fetch_image_by_id(img_id=img_id)

    return resp


@router.get('/system_load', response_model=SystemLoadOut)
async def system_load():
    ai_client = SDClient(config=config)

    resp = await ai_client.system_load()

    return resp
