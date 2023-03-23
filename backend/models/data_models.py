from typing import Optional

from pydantic import HttpUrl, Field

from .base_models import (
    BaseAliasedModel,
    BaseSDModelOut,
)


class Text2ImgIn(BaseAliasedModel):
    prompt: str = Field(example="Cute kitty", max_length=300)
    negative_prompt: Optional[str] = None
    width: Optional[int] = Field(default=512)
    height: Optional[int] = Field(default=512)
    samples: Optional[int] = Field(
        default=1,
        description="Number of images you want in response",
    )
    seed: Optional[int] = None


class Text2ImgOut(BaseSDModelOut):
    urls: Optional[list[HttpUrl]] = Field(alias="output")
    generation_time: Optional[float] = Field(alias="generationTime")


class FetchOut(BaseSDModelOut):
    urls: Optional[list[HttpUrl]] = Field(alias="output")


class SystemLoadOut(BaseSDModelOut):
    queue_time: Optional[float]
