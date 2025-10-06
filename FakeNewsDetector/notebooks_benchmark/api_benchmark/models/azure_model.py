import openai

openai.api_key = "TON_CLE"
openai.api_base = "https://ton-endpoint.openai.azure.com/"
openai.api_type = "azure"
openai.api_version = "2023-05-15"

def predict_azure(text: str) -> bool:
    prompt = f"Détecte si cette news est fausse : \"{text}\". Réponds seulement par 'FAKE' ou 'REAL'."
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    answer = response['choices'][0]['message']['content'].strip().lower()
    return "fake" in answer
