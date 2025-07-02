from typing import Literal

from pydantic import BaseModel

class SafetyDTO(BaseModel):
    is_safety: bool
    status: Literal['OK', 'REJECTED'] = 'OK'
    reason: str | None = None
    
    
    def to_dict(self):
        status = 'OK' if self.is_safety else 'REJECTED'
        response = self.model_dump(exclude={'is_safety'}, exclude_none=True)
        response['status'] = status
        return response
    
class ModerateResponse(BaseModel):
    status: Literal['OK', 'REJECTED']
    reason: str | None = None