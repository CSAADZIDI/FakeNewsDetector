from fastapi import FastAPI
from api_benchmark import model_router

app = FastAPI()
app.include_router(model_router.router)
