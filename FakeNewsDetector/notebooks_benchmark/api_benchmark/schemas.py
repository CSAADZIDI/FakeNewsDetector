from pydantic import BaseModel

class NewsRequest(BaseModel):
    content: str

class PredictionResponse(BaseModel):
    is_fake: bool
