from abc import ABC, abstractmethod


class IImageAIService(ABC):
    
    async def is_safety(self, image: bytes) -> dict:
        raise NotImplementedError