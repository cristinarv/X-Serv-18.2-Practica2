from django.db import models

# Create your models here.
class Urls(models.Model):
    url_original = models.CharField(max_length=64)
    def __str__(self):
        return self.url_original
