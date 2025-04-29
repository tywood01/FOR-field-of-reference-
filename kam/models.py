from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default="")
    description = models.TextField(default="")


class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=256, default="")
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True, related_name="pictures"
    )
