import base64
from django import forms
from django.core.files.base import ContentFile
from kam.models import Picture, Album


class ImageForm(forms.Form):
    image = forms.CharField(widget=forms.TextInput(attrs={"type": "hidden"}))
    album = forms.ModelChoiceField(
        queryset=Album.objects.none(),
        widget=forms.HiddenInput(),  # Make the album field hidden
        required=True,
    )

    def __init__(self, request, album_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        if album_id:
            album = Album.objects.filter(id=album_id).first()
            self.fields["album"].queryset = Album.objects.filter(id=album_id)
            self.fields[
                "album"
            ].initial = album  # Set the initial value to the album instance

    def save(self, commit=True):
        new_picture = Picture(album=self.cleaned_data["album"])
        image_data = self.cleaned_data["image"]

        # Decode the Base64 string (remove the prefix "data:image/png;base64,")
        format, imgstr = image_data.split(";base64,")  # Split the metadata and the data
        image_content = base64.b64decode(imgstr)  # Decode the Base64 string

        # Save the decoded image content to the model
        f1 = ContentFile(image_content)
        new_picture.image.save(
            "myphoto.png",
            f1,
            save=False,
        )

        if commit:
            new_picture.save()

        return new_picture


class AlbumForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
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
                    "cols": 60,
                    "placeholder": "fun album name! :)",
                    "maxlength": 255,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "cols": 60,
                    "placeholder": "fun album name! :)",
                    "maxlength": 255,
                }
            ),
        }
