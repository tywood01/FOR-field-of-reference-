from django.shortcuts import render
from kam.forms import PictureForm
# Create your views here.


def take_picture(request):
    """Create an image and submit it to the database."""

    if request.method == "POST":
        form = PictureForm(request, request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "kam/picture.html", {"form": form})
