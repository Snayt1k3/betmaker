import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.entrypoints.bet import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно настроить разрешенные адреса
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Подключение роутов
app.include_router(router, prefix="/api/bet", tags=["Bet"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
