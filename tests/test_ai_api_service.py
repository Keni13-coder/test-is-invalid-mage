import pytest
from infrastructure.ai_api_service import ImageAIService

@pytest.mark.asyncio(loop_scope='module')
@pytest.mark.parametrize('image_path, expected', [
    ('test_image_true.jpeg', True),
    ('test_image_false.jpeg', False)
    ]
)
async def test_is_safety(image_path: str, expected):
    '''Without information about the response format, the tests look incomplete.'''
    ai_api_service = ImageAIService()
    with open(f'images/{image_path}', 'rb') as image:
        response = await ai_api_service.is_safety(image.read())
    ...
    