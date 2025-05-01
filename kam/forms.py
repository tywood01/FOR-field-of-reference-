import base64
from django import forms
from django.core.files.base import ContentFile
from kam.models import Picture, Album


class ImageForm(forms.Form):
    image = forms.CharField(widget=forms.TextInput(attrs={"type": "hidden"}))

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def save(self, commit=True):
        new_picture = Picture(album=self.album)
        image_data = self.cleaned_data["image"]

        # Decode the Base64 string (remove the prefix "data:image/png;base64,")
        format, imgstr = image_data.split(";base64,")  # Split the metadata and the data
        image_content = base64.b64decode(imgstr)  # Decode the Base64 string
        print(image_content)
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
        fields = ['name', 'description']

        widgets = {
            "name" : forms.Textarea(
                attrs={
                    "rows" : 3,
                    "cols" : 60,
                    "placeholder" : "fun album name! :)",
                    "maxlength" : 255,
                }
            ),
            "description" : forms.Textarea(
                attrs={
                    "rows" : 3,
                    "cols" : 60,
                    "placeholder" : "fun album name! :)",
                    "maxlength" : 255,
                }
            ),
        
        }


