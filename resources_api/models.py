from django.db import models

class Resource(models.Model):
    topic = models.CharField(max_length=50)
    category = models.CharField(max_length=32)
    subcategory = models.CharField(max_length=50, null = True)
    URL = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.category + ": " + self.subcategory

class Forum(models.Model):
    name = models.CharField(max_length=32)
    question = models.TextField(max_length=500)

    def __str__(self):
        return self.question
    
