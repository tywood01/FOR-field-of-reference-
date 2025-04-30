from django.shortcuts import render
from kam.forms import Form
from django.http import HttpResponseRedirect
from .models import Picture
# Create your views here.


def take_picture(request):
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


def picture_gallery(request):
    pictures = Picture.objects.all()
    return render(request, "kam/gallery.html", {"pictures": pictures})


def manifest(request):
    """Render the manifest file."""

    return render(request, "kam/manifest.json", content_type="application/json")


def service_worker(request):
    """Render the service worker file."""

    return render(
        request, "kam/serviceworker.js", content_type="application/javascript"
    )
