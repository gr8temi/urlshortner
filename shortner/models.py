from django.db import models


# Create your models here.
class ShortURL(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=20, unique=True)
    short_url = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.original_url
