from django.test import SimpleTestCase
from django.urls import resolve, reverse
from main.views import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView


class TestUrls(SimpleTestCase):
    def test_url_home(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_url_sign_up(self):
        url = reverse("sign_up")
        self.assertEqual(resolve(url).func, sign_up)

    def test_url_login(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_url_logout(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_url_edit_password(self):
        url = reverse("edit_password")
        self.assertEqual(resolve(url).func.view_class, PasswordChangeView)

    def test_url_password_change_done(self):
        url = reverse("password_change_done")
        self.assertEqual(resolve(url).func, home)

    def test_url_edit_account(self):
        url = reverse("edit_account", args=[1])
        self.assertEqual(resolve(url).func, edit_account)

    def test_url_edit_profile(self):
        url = reverse("edit_profile", args=[1])
        self.assertEqual(resolve(url).func, edit_profile)

    def test_url_profile(self):
        url = reverse("user_profile", args=[1])
        self.assertEqual(resolve(url).func, user_profile)

    def test_url_add_post(self):
        url = reverse("add_post")
        self.assertEqual(resolve(url).func, add_post)

    def test_url_edit_post(self):
        url = reverse("edit_post", args=[1])
        self.assertEqual(resolve(url).func, edit_post)

    def test_url_delete_post(self):
        url = reverse("delete_post", args=[1])
        self.assertEqual(resolve(url).func, delete_post)

    def test_url_add_comment(self):
        url = reverse("add_comment", args=[1])
        self.assertEqual(resolve(url).func, add_comment)

    def test_url_delete_comment(self):
        url = reverse("delete_comment", args=[1])
        self.assertEqual(resolve(url).func, delete_comment)

    def test_url_thumb_up(self):
        url = reverse("thumb_up", args=[1])
        self.assertEqual(resolve(url).func, thumb_up)

    def test_url_search(self):
        url = reverse("search")
        self.assertEqual(resolve(url).func, search)

    def test_url_follow(self):
        url = reverse("follow", args=[1])
        self.assertEqual(resolve(url).func, follow)

    def test_url_unfollow(self):
        url = reverse("unfollow", args=[1])
        self.assertEqual(resolve(url).func, unfollow)
