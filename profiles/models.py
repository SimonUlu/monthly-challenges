from django.db import models

# Create your models here.


class UserProfile(models.Model):
    image = models.FileField(
        upload_to="images"
    )  ## it will take the file and store it to hard-drive and only the path to the db
