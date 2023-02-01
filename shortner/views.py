import json
from django.shortcuts import redirect
from .models import ShortURL
import random
import string
from django.http import JsonResponse


def shortener(request):
    if request.method == "POST":
        original_url = json.loads(request.body).get("original_url")
        code = "".join(random.choices(string.ascii_letters + string.digits, k=20))
        short_url = f"""{request.build_absolute_uri("/")}{code}"""
        data = {"original_url": original_url, "short_code": code, "short_url": short_url}
        ShortURL.objects.create(**data)
        return JsonResponse({"short_url": short_url})


def redirect_view(request, short_code):
    url = ShortURL.objects.get(short_code=short_code)
    return redirect(url.original_url)


def fetch_original_url(request):
    short_url = request.GET.get("url")
    url_data = ShortURL.objects.get(short_url=short_url)
    return JsonResponse({"original_url": url_data.original_url})
