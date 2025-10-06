from django.urls import path
from .views import analyse_news

urlpatterns = [
    path('', analyse_news, name="analyse-news"),
]
