from abc import ABC, abstractmethod
from typing import TypeVar

Safety = TypeVar('Safety')

class IAImageAIModeration(ABC):
    
    @abstractmethod
    async def is_safety(self, image) -> Safety:
        raise NotImplementedError