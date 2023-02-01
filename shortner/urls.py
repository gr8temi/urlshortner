from django.urls import path
from .views import shortener, redirect_view, fetch_original_url

urlpatterns = [
    path("", shortener, name="shortener"),
    path("retrieve/", fetch_original_url, name="fetch_original"),
    path("<str:short_code>/", redirect_view, name="redirect_view"),
]
