from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router as ai_image_router

def main():
    app = FastAPI(
        title='Image AI Moderation',
        description='Image AI Moderation',
        version='0.1.0',
        prefix='/api/v1'
    )
    
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"], # Не рекомендую использовать * в продакшене, видет за собой редкую ошибку CORS
    allow_headers=["*"], # Не рекомендую использовать * в продакшене, видет за собой редкую ошибку CORS
)
    
    app.include_router(ai_image_router)
       
    return app

app = main()