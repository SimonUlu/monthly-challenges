from django.db import models

# Create your models here.

class Book(models.Model):
    # it will automatically create an id field with autoincrementing number
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    