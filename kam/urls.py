"""
kam/urls.py

Authors: Tytus Woodburn
Emails: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01
Purpose:
    Provide view responses for the kam app.

"""

from django.urls import path
from . import views

app_name = "kam"
urlpatterns = [
    path("", views.take_picture, name="take_picture"),
    path("home", views.home, name="home"),
    path("gallery", views.picture_gallery, name="picture_gallery"),
    path("manifest.json", views.manifest, name="manifest"),
]
