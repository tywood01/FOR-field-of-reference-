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
    path("", views.home, name="home"),
    path("albums", views.all_albums, name="all_albums"),
    path("albums/create", views.create_album, name="create_album"),
    path("<int:user_id>/<int:album_id>/edit", views.edit_album, name="edit_album"),
    path("<int:user_id>/<int:album_id>/snap", views.take_picture, name="take_picture"),
    path("<int:user_id>/<int:album_id>/gallery", views.picture_gallery, name="picture_gallery"),
    path("manifest.json", views.manifest, name="manifest"),
]
