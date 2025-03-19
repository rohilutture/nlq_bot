from django.urls import path
from .views import nlq_bot_view

urlpatterns = [
    path("", nlq_bot_view, name="nlq_bot"),
]
