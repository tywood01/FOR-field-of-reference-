"""
    kam/views.py
    
    -Authors: Tytus Woodburn, Aaron Cumming, Ethan L'Heureux
    -Emails: tytus.woodburn@student.cune.edu, aaron.cumming@student.cune.edu, ethan.lheureux@student.cune.edu
    -Date: 05-05-2025
"""
from django.shortcuts import render, redirect
from kam.forms import AlbumForm, ImageForm
from django.http import HttpResponseRedirect
from .models import Picture, Album
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Placeholder for editing an album (not yet implemented)
def edit_album(request):
    pass


@login_required
def create_album(request):
    """Allow a logged-in user to create a new album."""
    form = AlbumForm(request)

    if request.method == "POST":
        form = AlbumForm(request, request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user  # Assign current user as the album owner
            album.save()
            return HttpResponseRedirect(reverse("kam:all_albums"))

        print(form.errors)  # Log form errors if invalid

    return render(request, "kam/create_album.html", {"form": form})


def take_picture(request, album_id):
    """Capture and save a picture to a specific album."""
    form = ImageForm(request, album_id=album_id)

    if request.method == "POST":
        form = ImageForm(request, album_id=album_id, data=request.POST, files=request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return HttpResponseRedirect(f"/kam/albums/{album_id}/gallery")

        print(form.errors)  # Log form errors if invalid

    return render(request, "kam/picture.html", {"form": form})


def home(request):
    """Render the home page."""
    return render(request, "kam/home.html")


def picture_gallery(request, album_id):
    """Display all pictures in a specific album."""
    pictures = Picture.objects.filter(album_id=album_id)

    context = {
        "pictures": pictures,
        "album": Album.objects.get(id=album_id),
        "album_url": f"/kam/albums/{album_id}/gallery",
    }

    return render(request, "kam/gallery.html", context)


@login_required
def all_albums(request):
    """List all albums owned by the logged-in user."""
    albums = Album.objects.filter(owner=request.user)
    return render(request, "kam/all_albums.html", {"albums": albums})


def manifest(request):
    """Serve the PWA manifest file."""
    return render(request, "kam/manifest.json", content_type="application/json")


def service_worker(request):
    """Serve the PWA service worker script."""
    return render(request, "kam/serviceworker.js", content_type="application/javascript")
