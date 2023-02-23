from django.test import TestCase
from main.forms import *

from django.core.files.base import File
from io import BytesIO
from PIL import Image


class TestForms(TestCase):
    @staticmethod
    def get_image_file(ext='png'):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=(50, 50))
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name='test.png')

    # tests for UserRegistrationForm form
    def test_forms_UserRegistrationForm_fields_max_length(self):
        form = UserRegistrationForm()
        first_name_max_len = form.fields['first_name'].max_length
        self.assertEqual(first_name_max_len, 30)

        last_name_max_len = form.fields['last_name'].max_length
        self.assertEqual(last_name_max_len, 30)

        email_max_len = form.fields['email'].max_length
        self.assertEqual(email_max_len, 254)

    def test_forms_UserRegistrationForm_valid_data(self):
        form = UserRegistrationForm(data={
            'username': 'Johnny',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'example@example.com',
            'password1': 'PasswordExample123!',
            'password2': 'PasswordExample123!'  
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)

    def test_forms_UserRegistrationForm_no_valid_data(self):
        form = UserRegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    # tests for UserProfileForm form
    def test_forms_UserProfileForm_valid_data(self):
        form = UserProfileForm(data={
            'gender': 0,
            'description': 'Test description',
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)

    def test_forms_UserProfileForm_no_valid_data(self):
        form = UserProfileForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    # tests for PostForm form
    def test_forms_PostForm_valid_data(self):
        img=self.get_image_file()
        data = {'post_img': img, 'description': 'description'}
        form = PostForm(data=data, files=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)

    def test_forms_PostForm_no_valid_data(self):   
        form = PostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    # tests for CommentForm form
    def test_forms_CommentForm_valid_data(self):
        form = CommentForm(data={
                'text': 'Test description'
            })

        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)

    def test_forms_CommentForm_no_valid_data(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)