from fastapi import APIRouter, UploadFile, File

from api.dtos import SafetyDTO
from .depends import dep_image_ai_moderation

router = APIRouter(prefix='/ai', tags=['AI'])

@router.post('/moderate')
async def moderate(
    image_ai_moderation: dep_image_ai_moderation,
    image: UploadFile = File(...)):
    result: SafetyDTO = await image_ai_moderation.is_safety(image)    
    
    return result.to_dict()