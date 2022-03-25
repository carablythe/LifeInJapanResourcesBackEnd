from django.db import models

# Create your models here.
class Resource(models.Model):
    topic = models.CharField(max_length=50)
    category = models.CharField(max_length=32)
    subcategory = models.CharField(max_length=50, null = True)
    URL = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

class Forum(models.Model):
    name = models.CharField(max_length=32)
    question = models.TextField(max_length=500)
