"""
    kam/models.py
    
    -Authors: Tytus Woodburn, Ethan L'Heureux
    -Emails: tytus.woodburn@student.cune.edu, ethan.lheureux@student.cune.edu
    -Date: 05-05-2025
"""
from django.db import models
from django.contrib.auth.models import User
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default="")
    description = models.TextField(default="")

    pictures: "RelatedManager[Picture]"


class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=256, default="")
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="pictures"
    )
