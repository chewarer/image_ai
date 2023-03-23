from enum import Enum

from pydantic import BaseSettings


class Env(str, Enum):
    dev = "dev"
    prod = "prod"


class AIService(str, Enum):
    sd = "sd"
    midjourney = "midjourney"


class AppConfig(BaseSettings):
    VERSION: str = "0.0.1"
    ENV: Env = Env.dev
    DEBUG: bool = False
    AI: AIService = AIService.sd

    # Stable Diffusion config
    SD_API_URL: str = "https://stablediffusionapi.com/api"
    SD_API_VER: str = "v3"
    SD_API_KEY: str = None


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
