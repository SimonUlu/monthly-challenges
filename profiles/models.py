from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.FileField() ## it will take the file and store it to harddrive and only the path to the db
