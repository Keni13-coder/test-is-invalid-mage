from typing import Annotated
from fastapi import Depends
from infrastructure.ai_api_service import ImageAIService
from application.image_ai_moderation import ImageAIModeration


def get_image_ai_moderation() -> ImageAIModeration:
    return ImageAIModeration(ImageAIService())


dep_image_ai_moderation = Annotated[ImageAIModeration, Depends(get_image_ai_moderation)]