from fastapi import FastAPI
from fastapi_api.schemas import NewsRequest, PredictionResponse
from fastapi_api.model import is_fake_news

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
def predict(news: NewsRequest):
    result = is_fake_news(news.content)
    return {"is_fake": result}
