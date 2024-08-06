from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Author(models.Model):
    # id will be created auto
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    

class Book(models.Model):
    # it will automatically create an id field with autoincrementing number
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
    
    
    