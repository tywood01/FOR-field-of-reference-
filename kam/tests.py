"""
    kam/tests.py
    
    -Authors: Tytus Woodburn, Andrew Fynaardt
    -Emails: tytus.woodburn@student.cune.edu, andrew.fynaardt@student.cune.edu
    -Date: 05-05-2025
"""
from django.test import TestCase
from django.core.files.base import ContentFile
from kam.forms import Form
from kam.models import Picture
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

    def test_form_save(self):
        # Create the form with the sample image data
        form_data = {"image": self.sample_image_data}
        form = Form(self.request, data=form_data)

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
