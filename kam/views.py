from django.shortcuts import render
from kam.forms import Form
from django.http import HttpResponseRedirect

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
