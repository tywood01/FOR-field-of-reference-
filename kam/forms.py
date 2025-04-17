"""
forms.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Define reusable forms for the kam app.

"""

from django import forms
from kam.models import picture


class PictureForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.instance.user = request.user

    class Meta:
        model = picture
        fields = ["image"]
