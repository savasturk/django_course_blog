from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=160)
    text = models.TextField()
    author = models.CharField(max_length=25)
    tarih = models.DateTimeField(auto_now_add=True)

