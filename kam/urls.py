"""
    kam/urls.py

    -Authors: Tytus Woodburn, Aaron Cumming, Ethan L'Heureux
    -Emails: tytus.woodburn@student.cune.edu, aaron.cumming@student.cune.edu, ethan.lheureux@student.cune.edu
    -Purpose:
        Provide view responses for the kam app.
    -Date:05-05-2025

"""

from django.urls import path, include
from . import views

app_name = "kam"
urlpatterns = [
    path("", views.home, name="home"),
    path("albums", views.all_albums, name="all_albums"),
    path("albums/create/", views.create_album, name="create_album"),
    path("albums/<int:album_id>/gallery", views.picture_gallery, name="picture_gallery"),
    path("albums/<int:album_id>/edit", views.edit_album, name="edit_album"),
    path("albums/<int:album_id>/snap", views.take_picture, name="take_picture"),
    path("manifest.json", views.manifest, name="manifest"),
    path("qr-code/", include("qr_code.urls", namespace="qr_code")),
]
