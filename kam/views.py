from django.shortcuts import render, redirect
from kam.forms import AlbumForm, ImageForm
from django.http import HttpResponseRedirect
from .models import Picture, Album
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


def edit_album(request):
    pass


@login_required
def create_album(request):
    form = AlbumForm(request)

    if request.method == "POST":
        form = AlbumForm(
            request,
            request.POST,
        )

        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user
            album.save()

            return HttpResponseRedirect(reverse("kam:all_albums"))
        print(form.errors)

    return render(
        request,
        "kam/create_album.html",
        {
            "form": form,
        },
    )


def take_picture(request, album_id):
    form = ImageForm(request, album_id=album_id)

    if request.method == "POST":
        form = ImageForm(
            request, album_id=album_id, data=request.POST, files=request.FILES
        )
        if form.is_valid():
            instance = form.save()
            instance.save()

            return HttpResponseRedirect(f"/kam/albums/{album_id}/gallery")

        print(form.errors)

    return render(request, "kam/picture.html", {"form": form})


def home(request):
    """Render the home page."""

    return render(request, "kam/home.html")


def picture_gallery(request, album_id):
    """Display all pictures in a specific album."""
    pictures = Picture.objects.filter(album_id=album_id)
    album = Album.objects.get(id=album_id)
    return render(request, "kam/gallery.html", {"pictures": pictures, "album": album})


@login_required
def all_albums(request):
    albums = Album.objects.filter(owner=request.user)
    return render(request, "kam/all_albums.html", {"albums": albums})


def manifest(request):
    """Render the manifest file."""

    return render(request, "kam/manifest.json", content_type="application/json")


def service_worker(request):
    """Render the service worker file."""

    return render(
        request, "kam/serviceworker.js", content_type="application/javascript"
    )
