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
        self.client.logout()
        response = self.client.get(reverse('sign_up'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')

    def test_views_sign_up_POST_correct_data(self):
        self.client.logout()
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
        self.client.logout()
        response = self.client.post(reverse('sign_up'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')
        self.assertEqual(User.objects.count(), 1) # value=1, because of creation user1 in setUp
        self.assertEqual(UserProfile.objects.count(), 1) # value=1, because of creation user1_profile in setUp

    def test_views_edit_account_GET_positive(self):
        response = self.client.get(reverse('edit_account', args=[1]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/edit_account.html')

    def test_views_edit_account_GET_negative(self):
        response = self.client.get(reverse('edit_account', args=[2]))
        
        self.assertEqual(response.status_code, 302)

    def test_views_edit_account_POST(self):
        response = self.client.post(reverse('edit_account', args=[1]), {
            'username': 'Johnny',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john@example.com'
        })

        user = User.objects.get(id=1)

        self.assertEqual(response.status_code, 302) 
        self.assertEqual(user.username, 'Johnny')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Smith')
        self.assertEqual(user.email, 'john@example.com')

    def test_views_edit_profile_GET(self):
        response = self.client.get(reverse('edit_profile', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/edit_profile.html')

    def test_views_edit_profile_POST_correct_data(self):
        response = self.client.post(reverse('edit_profile', args=[1]), {
            'gender': '1',
            'description': 'Testing',
            'profile_img': 'profile_imgs/default_male.jpg'

        })

        user_profile = UserProfile.objects.get(id=1)

        self.assertEqual(response.status_code, 302)

        self.assertEqual(user_profile.gender, 1)
        self.assertEqual(user_profile.description, 'Testing')
        self.assertEqual(user_profile.profile_img, 'profile_imgs/default_male.jpg')

    def test_views_edit_profile_POST_incorrect_data(self):
        response = self.client.post(reverse('edit_profile', args=[1]))

        user_profile = UserProfile.objects.get(id=1)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/edit_profile.html')

        self.assertEqual(user_profile.gender, 0)
        self.assertEqual(user_profile.description, '')
        self.assertEqual(user_profile.profile_img, 'profile_imgs/default_male.jpg')
        