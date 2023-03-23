import io

import aiohttp

from models.data_models import (
    Text2ImgIn,
    Text2ImgOut,
    FetchOut,
    SystemLoadOut,
)
from .base import ClientFabric


mocked_prompt = "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy " \
                "black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic " \
                "lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, " \
                "1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K"

default_negative_prompts = [
    "((out of frame))",
    "((extra fingers))",
    "mutated hands",
    "((poorly drawn hands))",
    "((poorly drawn face))",
    "(((mutation)))",
    "(((deformed)))",
    "(((tiling)))",
    "((tile))",
    "((fleshpile))",
    "((ugly))",
    "(((abstract)))",
    "blurry",
    "((bad anatomy))",
    "((bad proportions))",
    "((extra limbs))",
    "cloned face",
    "(((skinny)))",
    "glitchy",
    "((extra breasts))",
    "((double torso))",
    "((extra arms))",
    "((extra hands))",
    "((mangled fingers))",
    "((missing breasts))",
    "(missing lips)",
    "((ugly face))",
    "((fat))",
    "((extra legs))",
    "anime",
]

default_negative_prompts_str = ", ".join(default_negative_prompts)


class SDClient(ClientFabric):
    """Stable Diffusion client"""
    async def text_to_image(self, params: Text2ImgIn) -> Text2ImgOut:
        url = f"{self.config.SD_API_URL}/{self.config.SD_API_VER}/text2img"
        negative_prompt = params.negative_prompt or default_negative_prompts_str

        body = dict(
            key=self.config.SD_API_KEY,
            prompt=mocked_prompt,
            negative_prompt=negative_prompt,
            width=params.width,
            height=params.height,
            samples=params.samples,
            seed=params.seed,
            num_inference_steps="20",
            guidance_scale=7.5,
            safety_checker="yes",
            webhook=None,
            track_id=None,
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, data=body) as resp:
                data: dict = await resp.json()

        return Text2ImgOut(**data)

    async def image_to_image(self, prompt: str, image: io.BytesIO) -> dict:
        return {}

    async def fetch_image_by_id(self, img_id: int):
        url = f"{self.config.SD_API_URL}/{self.config.SD_API_VER}/fetch/{img_id}"
        body = dict(
            key=self.config.SD_API_KEY,
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, data=body) as resp:
                data: dict = await resp.json()

        return FetchOut(**data)

    async def system_load(self):
        url = f"{self.config.SD_API_URL}/{self.config.SD_API_VER}/system_load"
        body = dict(
            key=self.config.SD_API_KEY,
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, data=body) as resp:
                data: dict = await resp.json()

        return SystemLoadOut(**data)
