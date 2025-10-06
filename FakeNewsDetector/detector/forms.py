from django import forms

class NewsForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Entrez votre news")
