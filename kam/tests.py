"""
    kam/tests.py
    
    -Authors: Tytus Woodburn, Andrew Fynaardt
    -Emails: tytus.woodburn@student.cune.edu, andrew.fynaardt@student.cune.edu
    -Date: 05-05-2025
"""
from django.test import TestCase, RequestFactory
from django.core.files.base import ContentFile
from kam.forms import ImageForm, AlbumForm
from kam.models import Picture, Album, User
from faker import Faker
import base64

faker = Faker()


class PictureFormTestCase(TestCase):
    def setUp(self):
        # Create a sample Base64-encoded image string
        self.sample_image_data = "data:image/png;base64," + base64.b64encode(
            b"fake_image_data"
        ).decode("utf-8")
        self.request = None  # Mock request object if needed

        # Create a temporary album for testing
        self.user = User.objects.create_user(username="testuser", password="password")
        self.album = Album.objects.create(
            owner=self.user, name="Temporary Album", description="Temporary description"
        )

    def test_form_save(self):
        # Create the form with the sample image data and album ID
        form_data = {"image": self.sample_image_data, "album": self.album.id}
        form = ImageForm(self.request, album_id=self.album.id, data=form_data)

        # Ensure the form is valid
        self.assertTrue(form.is_valid())

        # Save the form and retrieve the saved picture instance
        instance = form.save()
        instance.save()
        instance.refresh_from_db()

        # Check that the picture instance is saved correctly
        self.assertIsInstance(instance, Picture)
        self.assertIsNotNone(instance.pk)

        # Check that the image content is saved correctly
        with instance.image.open("rb") as img_file:
            saved_content = img_file.read()
            expected_content = base64.b64decode(self.sample_image_data.split(",")[1])
            self.assertEqual(saved_content, expected_content)

class AlbumFormTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_album_form_valid(self):
        request = self.factory.get('/')
        request.user = self.user

        form_data = {
            'name': 'Test Album',
            'description': 'This is a test description for the album.'
        }
        form = AlbumForm(request=request, data=form_data)

        self.assertTrue(form.is_valid())
        album = form.save(commit=False)
        self.assertEqual(album.name, 'Test Album')
        self.assertEqual(album.description, 'This is a test description for the album.')
        self.assertEqual(album.user, self.user)

    def test_album_form_invalid(self):
        request = self.factory.get('/')
        request.user = self.user

        form_data = {
            'name': '',  # Name is required, so this should make the form invalid
            'description': 'This is a test description for the album.'
        }
        form = AlbumForm(request=request, data=form_data)

        self.assertFalse(form.is_valid())