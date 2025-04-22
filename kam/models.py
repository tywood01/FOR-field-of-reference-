from django.db import models


# Create your models here.
class picture(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=256, default="")
