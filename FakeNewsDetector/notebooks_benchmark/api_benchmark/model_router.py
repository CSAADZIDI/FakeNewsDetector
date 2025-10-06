from fastapi import APIRouter
from api_benchmark.schemas import NewsRequest, PredictionResponse
from api_benchmark.models import tfidf_model, bert_model, azure_model

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(news: NewsRequest, method: str = "tfidf"):
    if method == "tfidf":
        result = tfidf_model.predict_tfidf(news.content)
    elif method == "bert":
        result = bert_model.predict_bert(news.content)
    elif method == "azure":
        result = azure_model.predict_azure(news.content)
    else:
        raise ValueError("Méthode non supportée.")
    return {"is_fake": result}
