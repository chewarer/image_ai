from abc import ABC
import io

from pydantic import BaseModel

from config import AppConfig
from ..models.data_models import Text2ImgOut


class ClientFabric(ABC):
    def __init__(self, config: AppConfig):
        self.config = config
        self.ai_client = config.AI

    async def text_to_image(self, params: BaseModel) -> Text2ImgOut:
        """Pass request to AI srvice to generate image from text"""
        raise NotImplementedError

    async def image_to_image(self, prompt: str, image: io.BytesIO) -> dict:
        """Pass request to AI service to generate image from image"""
        raise NotImplementedError
