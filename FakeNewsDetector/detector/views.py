from django.shortcuts import render


from .forms import NewsForm
import requests

def analyse_news(request):
    result = None
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # Envoi vers FastAPI
            try:
                response = requests.post("http://localhost:8001/predict", json={"content": content})
                if response.status_code == 200:
                    result = "Fake" if response.json()['is_fake'] else "Not Fake"
                else:
                    result = "Erreur de l'API"
            except Exception as e:
                result = f"Erreur : {e}"
    else:
        form = NewsForm()

    return render(request, "detector/form.html", {"form": form, "result": result})

