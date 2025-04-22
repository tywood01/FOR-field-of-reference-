from django.db import models


# Create your models here.
class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=256, default="")
