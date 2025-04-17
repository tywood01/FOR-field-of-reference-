from django.shortcuts import render
from kam.forms import PictureForm
from django.http import HttpResponseRedirect

# Create your views here.


def take_picture(request):
    """Create an image and submit it to the database."""

    form = PictureForm(request, request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/kam/home")

    return render(request, "kam/picture.html", {"form": form})


def home(request):
    """Render the home page."""

    return render(request, "kam/home.html")
