import os
from enum import Enum

from pydantic import BaseSettings


root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

env_file = f'{root_dir}/.env'
if not os.path.exists(env_file):
    env_file = None


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
        env_file = env_file
        env_file_encoding = 'utf-8'
