from django.test import TestCase, Client
from django.urls import reverse
from main.models import UserProfile, Follow, Post, Comment, Like
from django.contrib.auth.models import User
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='David', 
            first_name='David',
            last_name='Jones',
            email='david@example.com',
            password='PasswordExample123!'
        )
        self.user1_profile = UserProfile.objects.create(user=self.user1)
        self.logged_in = self.client.login(username=self.user1.username, password='PasswordExample123!')

    def test_loggin_user(self):
        self.assertTrue(self.logged_in)

    def test_views_home_GET(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

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
        self.assertEqual(User.objects.get(id=2).first_name, 'John')
        self.assertEqual(UserProfile.objects.get(id=2).user.username, 'Johnny')

    def test_views_sign_up_POST_incorrect_data(self):
        response = self.client.post(reverse('sign_up'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')
        self.assertEqual(User.objects.count(), 1) # value=1, because of creation user1 in setUp
        self.assertEqual(UserProfile.objects.count(), 1) # value=1, because of creation user1_profile in setUp