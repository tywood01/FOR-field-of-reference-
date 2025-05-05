"""
    kam/admin.py

    -Authors: Tytus Woodburn
    -Emails: tytus.woodburn@student.cune.edu
    -Date: 05-05-2025
"""
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Picture)
admin.site.register(models.Album)