import io

import aiohttp

from .lib import (
    prettified_prompt_str,
    default_negative_prompts_str,
)
from ..models.data_models import (
    Text2ImgIn,
    Text2ImgOut,
    FetchOut,
    SystemLoadOut,
)
from .base import ClientFabric


mocked_prompt = "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy " \
                "black eyeliner)), blue eyes, shaved side haircut, magic neon, dark red city"

mocked_response = {
    'status': 'success',
    'generationTime': 2.6407310962677,
    'id': 7692181,
    'output': ['https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d6393b54'
               '-040a-4e67-a3a8-75f641288157-0.png'],
    'meta': {'H': 512,
             'W': 512,
             'enable_attention_slicing': 'true',
             'file_prefix': 'd6393b54-040a-4e67-a3a8-75f641288157',
             'guidance_scale': 7.5,
             'model': 'runwayml/stable-diffusion-v1-5',
             'n_samples': 1,
             'negative_prompt': '',
             'outdir': 'out',
             'prompt': 'ultra realistic close up portrait ((beautiful pale cyberpunk '
                       'female with heavy black eyeliner)), blue eyes, shaved side '
                       'haircut, hyper detail, cinematic lighting, magic neon, dark red '
                       'city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, '
                       'unedited, symmetrical balance, in-frame, 8K',
             'revision': 'fp16',
             'safetychecker': 'yes',
             'seed': 3469051683,
             'steps': 20,
             'vae': 'stabilityai/sd-vae-ft-mse'}
}


class SDClient(ClientFabric):
    """Stable Diffusion client"""
    async def text_to_image(self, params: Text2ImgIn) -> Text2ImgOut:
        if params.use_default_negative_prompt:
            negative_prompt = params.negative_prompt
        else:
            negative_prompt = default_negative_prompts_str

        # prompt = params.prompt
        prompt = mocked_prompt

        if params.prettify_prompt:
            prompt = ", ".join((prompt, prettified_prompt_str))

        url = f"{self.config.SD_API_URL}/{self.config.SD_API_VER}/text2img"

        body = dict(
            key=self.config.SD_API_KEY,
            prompt=prompt,
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

        # data = mocked_response

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
