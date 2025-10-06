import joblib

model = joblib.load("tfidf_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_tfidf(text: str) -> bool:
    X = vectorizer.transform([text])
    return model.predict(X)[0] == 1  # Fake = 1