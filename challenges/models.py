from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    # it will automatically create an id field with autoincrementing number
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=255)
    is_bestselling = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
    