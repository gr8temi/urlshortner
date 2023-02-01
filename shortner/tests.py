from django.test import TestCase, Client

from .models import ShortURL
import json
from django.urls import reverse


class ShortenerTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        ShortURL.objects.create(
            original_url="https://www.google.com/",
            short_code="abc123",
            short_url="http://a.com/abc123",
        )

    def test_shortener(self):
        response = self.client.post(
            reverse("shortener"),
            content_type="application/json",
            data={"original_url": "https://www.example.co/"},
        )
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn("short_url", response_data)

        short_url = response_data["short_url"]
        short_url_obj = ShortURL.objects.get(short_url=short_url)
        self.assertEqual(short_url_obj.original_url, "https://www.example.co/")

    def test_redirect_view(self):
        response = self.client.get("/abc123/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "https://www.google.com/")

    def test_fetch_original_url(self):
        response = self.client.get(reverse("fetch_original"), {"url": "http://a.com/abc123"})
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn("original_url", response_data)
        self.assertEqual(response_data["original_url"], "https://www.google.com/")
