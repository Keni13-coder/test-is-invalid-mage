from json import JSONDecodeError

from httpx import AsyncClient
from loguru import logger

from interfaces.ai_api_service import IImageAIService
from config import settings

class ImageAIService(IImageAIService):
    
    async def is_safety(self, image: bytes) -> dict:
        async with AsyncClient() as client:
            response = await client.post(
                settings.AI_URL,
                headers={'api-key': settings.AI_KEY},
                files={
                    'image': image,
                    }
            )
            try:
                result = response.json()
            except JSONDecodeError:
                logger.error(response.text)
                result = {}
                
            return result