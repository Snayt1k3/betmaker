import uvicorn
from fastapi import FastAPI

from src.entrypoints.bet import router

app = FastAPI()

# Подключение роутов
app.include_router(router, prefix="/api/bet", tags=["Bet"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
