from fastapi import UploadFile

from interfaces.image_ai_moderation import IAImageAIModeration
from interfaces.ai_api_service import IImageAIService
from api.dtos import SafetyDTO

class ImageAIModeration(IAImageAIModeration):
    def __init__(
        self,
        ai_api_service: IImageAIService
        ):
        self._ai_api_service = ai_api_service
        
    async def __extract_data(self, response: dict) -> SafetyDTO:
        '''
        It is a stub because there is no information about the format of the returned data.
        link https://deepai.org/machine-learning-model/nsfw-detector -> 403 and raise CORS
        '''
        ...
        
    async def is_safety(self, image: UploadFile) -> SafetyDTO:
        image = await image.read()
        response: dict = await self._ai_api_service.is_safety(image)
        
        return await self.__extract_data(response)
    