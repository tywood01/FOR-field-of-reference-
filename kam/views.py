from django.shortcuts import render
from kam.forms import Form
from django.http import HttpResponseRedirect
from .models import Picture, Album
from django.contrib.auth.decorators import login_required
# Create your views here.

def edit_album(request):
    pass

def take_picture(request, user_id, album_id):
    """Create an image and submit it to the database."""

    form = Form(request)

    if request.method == "POST":
        form = Form(request, request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return HttpResponseRedirect("/kam/home")

        print(form.errors)

    return render(request, "kam/picture.html", {"form": form})


def home(request):
    """Render the home page."""

    return render(request, "kam/home.html")


def picture_gallery(request, user_id, album_id):
    pictures = Picture.objects.all()
    return render(request, "kam/gallery.html", {"pictures": pictures})


@login_required
def all_albums(request):
    
    albums = Album.objects.filter(
        owner = request.user
    )
    return render(request, "kam/all_albums.html", {"albums": albums})


def manifest(request):
    """Render the manifest file."""

    return render(request, "kam/manifest.json", content_type="application/json")


def service_worker(request):
    """Render the service worker file."""

    return render(
        request, "kam/serviceworker.js", content_type="application/javascript"
    )
