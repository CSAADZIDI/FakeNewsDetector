from transformers import pipeline

classifier = pipeline("text-classification", model="bert-base-uncased")

def predict_bert(text: str) -> bool:
    result = classifier(text)[0]
    return result['label'].lower() == 'fake'
