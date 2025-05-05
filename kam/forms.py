"""
    kam/forms.py
    
    -Authors: Tytus Woodburn, Ethan L'Heureux
    -Emails: tytus.woodburn@student.cune.edu, ethan.lheureux@student.cune.edu
    -Date: 05-05-2025
"""
import base64
from django import forms
from django.core.files.base import ContentFile
from kam.models import Picture, Album


class ImageForm(forms.Form):
    """
    A form that accepts a base64-encoded image and a hidden album ID to save a Picture instance.
    """

    # Hidden input that stores the base64-encoded image data from the front end
    image = forms.CharField(widget=forms.TextInput(attrs={"type": "hidden"}))

    # Hidden field to associate the image with a specific album
    album = forms.ModelChoiceField(
        queryset=Album.objects.none(),
        widget=forms.HiddenInput(),
        required=True,
    )

    def __init__(self, request, album_id, *args, **kwargs):
        """
        Custom initializer that:
        """
        super().__init__(*args, **kwargs)
        self.request = request
        if album_id:
            album = Album.objects.filter(id=album_id).first()
            self.fields["album"].queryset = Album.objects.filter(id=album_id)
            self.fields["album"].initial = album

    def save(self, commit=True):
        """
        Saves the base64-encoded image as a Picture instance.
        """

        new_picture = Picture(album=self.cleaned_data["album"])
        image_data = self.cleaned_data["image"]

        # Extract base64 data after the header (e.g., "data:image/png;base64,")
        format, imgstr = image_data.split(";base64,")
        image_content = base64.b64decode(imgstr)

        # Create ContentFile from decoded image and save to Picture model
        f1 = ContentFile(image_content)
        new_picture.image.save("myphoto.png", f1, save=False)

        if commit:
            new_picture.save()

        return new_picture


class AlbumForm(forms.ModelForm):
    """
    A form for creating a new Album associated with the logged-in user.
    """

    def __init__(self, request, *args, **kwargs):
        """
        Custom initializer to attach the request and set the album owner.
        """
        super().__init__(*args, **kwargs)
        self.request = request
        self.instance.user = request.user

    class Meta:
        model = Album
        fields = ["name", "description"]

        widgets = {
            "name": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Name this album!",
                    "maxlength": 255,
                    "class": "w-full resize-none rounded-lg border border-gray-300 p-2 focus:outline-none focus:ring-2 focus:ring-black",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Make a description for this album!",
                    "maxlength": 255,
                    "class": "w-full resize-none rounded-lg border border-gray-300 p-2 focus:outline-none focus:ring-2 focus:ring-black",
                }
            ),
        }