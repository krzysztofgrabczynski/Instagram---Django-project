from django.test import TestCase, Client
from django.urls import reverse
from main.models import UserProfile, Follow, Post, Comment, Like
from django.contrib.auth.models import User
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_views_sign_up_GET(self):
        response = self.client.get(reverse('sign_up'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')

    def test_views_sign_up_POST_correct_data(self):
        response = self.client.post(reverse('sign_up'), {
            'username': 'Johnny', 
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john@example.com',
            'password1': 'PasswordExample123!',
            'password2': 'PasswordExample123!'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.first().first_name, 'John')
        self.assertEqual(UserProfile.objects.first().user.username, 'Johnny')

    def test_views_sign_up_POST_incorrect_data(self):
        response = self.client.post(reverse('sign_up'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(UserProfile.objects.count(), 0)