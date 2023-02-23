from django.test import TestCase, Client
from django.urls import reverse
from main.models import UserProfile, Follow, Post, Comment, Like
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user_1 = User.objects.create_user(
            username='David', 
            first_name='David',
            last_name='Jones',
            email='david@example.com',
            password='PasswordExample123!'
        )
        self.test_user_1_profile = UserProfile.objects.create(user=self.test_user_1)
        self.logged_in = self.client.login(username=self.test_user_1.username, password='PasswordExample123!')

        self.test_user_2 = User.objects.create_user(
            username='test_username_1', 
            first_name='test_first_name_1',
            last_name='test_last_name_1',
            email='test1@example.com',
            password='PasswordExample123!'
        )
        self.test_user_2_profile = UserProfile.objects.create(user=self.test_user_2)

    def test_loggin_user(self):
        self.assertTrue(self.logged_in)

    # tests for home view
    def test_views_home_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('home'))

        self.assertRedirects(response, '/instagram/login/?next=/instagram/')

    def test_views_home_GET(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_views_home_context(self):
        test_post = Post.objects.create(user=self.test_user_2, description='test description')
        Follow.objects.create(user=self.test_user_1, user_followed=self.test_user_2, followd_user_id=self.test_user_2.id)
        test_comment = Comment.objects.create(post=test_post, user=self.test_user_1, text='test comment')

        response = self.client.get(reverse('home'))

        self.assertEqual(response.context['posts'].first(), Post.objects.first())
        self.assertEqual(test_post.description, 'test description')
        self.assertEqual(response.context['users_comments'].first(), 1)
        self.assertEqual(test_comment.text, 'test comment')
        
    # tests for sign_up view
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
        self.assertEqual(User.objects.get(id=3).first_name, 'John')
        self.assertEqual(UserProfile.objects.get(id=3).user.username, 'Johnny')

    def test_views_sign_up_POST_incorrect_data(self):
        self.client.logout()
        response = self.client.post(reverse('sign_up'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')
        self.assertEqual(User.objects.count(), 2) # value=2, because of creation users in setUp
        self.assertEqual(UserProfile.objects.count(), 2) # value=2, because of creation profiles in setUp

    # tests for edit_account view
    def test_views_edit_account_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('edit_account', args=[1]))

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/edit_account/'))

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

    # tests for edit_profile view
    def test_views_edit_profile_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('edit_profile', kwargs={'id': self.test_user_1.id}))

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/edit_profile/'))

    def test_views_edit_profile_GET_404(self):
        response = self.client.get(reverse('edit_profile', kwargs={'id': 10}))

        self.assertEqual(response.status_code, 404)

    def test_views_edit_profile_GET(self):
        response = self.client.get(reverse('edit_profile', kwargs={'id': self.test_user_1.id}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/edit_profile.html')

    def test_views_edit_profile_POST_correct_data(self):
        response = self.client.post(reverse('edit_profile', kwargs={'id': self.test_user_1.id}), {
            'gender': '1',
            'description': 'Testing',
        })

        user_profile = UserProfile.objects.get(id=1)

        self.assertEqual(response.status_code, 302)

        self.assertEqual(user_profile.gender, 1)
        self.assertEqual(user_profile.description, 'Testing')
        self.assertEqual(user_profile.profile_img, 'profile_imgs/default_male.jpg')

    def test_views_edit_profile_POST_incorrect_data(self):
        response = self.client.post(reverse('edit_profile', kwargs={'id': self.test_user_1.id}))

        user_profile = UserProfile.objects.get(id=1)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/edit_profile.html')

        self.assertEqual(user_profile.gender, 0)
        self.assertEqual(user_profile.description, '')
        self.assertEqual(user_profile.profile_img, 'profile_imgs/default_male.jpg')

    # tests for user_profile view 
    def test_views_user_profile_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('user_profile', kwargs={'id': self.test_user_1.id}))

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/profile/'))

    def test_views_user_profile_GET(self):
        response = self.client.get(reverse('user_profile', kwargs={'id': self.test_user_1.id}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

    def test_views_user_profile_GET_context(self):
        Post.objects.create(user=self.test_user_1, description='test description')
        response = self.client.get(reverse('user_profile', kwargs={'id': self.test_user_1.id}))

        self.assertEqual(response.context['profile'], self.test_user_1_profile)
        self.assertEqual(response.context['gender'], 'male')
        self.assertEqual(list(response.context['posts']), list(self.test_user_1.posts.all()))
    
    def test_view_user_profile_follow_context_postivie(self):
        Follow.objects.create(user=self.test_user_1, user_followed=self.test_user_2, followd_user_id=self.test_user_2.id)
        response = self.client.get(reverse('user_profile', kwargs={'id': self.test_user_2.id}))

        self.assertTrue(response.context['is_followed'])
    
    def test_view_user_profile_follow_context_negative_v1(self):
        response = self.client.get(reverse('user_profile', kwargs={'id': self.test_user_1.id}))

        self.assertFalse(response.context['is_followed'])
    
    def test_view_user_profile_follow_context_negative_v2(self):
        response = self.client.get(reverse('user_profile', kwargs={'id': self.test_user_2.id}))

        self.assertFalse(response.context['is_followed'])

    # test for add_post view
    def test_views_add_post_if_not_logged_in(self):
            self.client.logout()
            response = self.client.get(reverse('add_post'))

            self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/add_post'))

    def test_view_add_post_GET(self):
        response = self.client.get(reverse('add_post'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_view_add_post_POST(self):
            with open('media_dir\posts_imgs\david_brown_post_1.jpg', 'rb') as img:
                response = self.client.post(reverse('add_post'), {
                    'post_img': img,
                    'description': 'post test description'
                })

            post = self.test_user_1.posts.first()    
            self.test_user_1_profile.refresh_from_db()
            
            self.assertEqual(response.status_code, 302)
            self.assertEqual(post.description, 'post test description')
            self.assertEqual(self.test_user_1_profile.posts_amount, self.test_user_1.posts.count())

    # test for add_post view
    def test_view_edit_post_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('edit_post', kwargs={'id': 1})) 

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/edit_post'))     

    def test_view_edit_post_GET(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        response = self.client.get(reverse('edit_post', kwargs={'id': test_post.id}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_post.html')

    def test_view_edit_post_404(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        response = self.client.get(reverse('edit_post', kwargs={'id': 2}))

        self.assertEqual(response.status_code, 404)

    def test_view_edit_post_if_logged_user_is_post_owner(self):
        test_post = Post.objects.create(user=self.test_user_2, description='test description')
        response = self.client.get(reverse('edit_post', kwargs={'id': test_post.id}))

        self.assertEqual(response.status_code, 302)

    def test_view_edit_post_POST_positive(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        with open('media_dir\posts_imgs\david_brown_post_1.jpg', 'rb') as img:
            response = self.client.post(reverse('edit_post', kwargs={'id': test_post.id}), {
                'post_img': img,
                'description': 'after editing'
            })
        test_post.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(test_post.description, 'after editing')
    
    def test_view_edit_post_POST_negative(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        response = self.client.post(reverse('edit_post', kwargs={'id': test_post.id}))

        self.assertEqual(response.status_code, 200)
    
    # test for delete_post view
    def test_view_delete_post_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('delete_post', kwargs={'id': 1})) 

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/delete_post'))  

    def test_view_delete_post_if_logged_user_is_post_owner(self):
        test_post = Post.objects.create(user=self.test_user_2, description='test description')
        response = self.client.get(reverse('delete_post', kwargs={'id': test_post.id}))

        self.assertEqual(response.status_code, 302)

    def test_view_delete_post(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        self.test_user_1_profile.posts_amount += 1
        self.test_user_1_profile.save()
        
        self.client.get(reverse('delete_post', kwargs={'id': test_post.id}))

        self.test_user_1_profile.refresh_from_db()
        
        self.assertEqual(self.test_user_1_profile.posts_amount, 0)
        self.assertEqual(Post.objects.count(), 0)

    # test for add_comment view
    def test_view_add_comment_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('add_comment', kwargs={'post_id': 1})) 

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/add_comment')) 

    def test_view_add_comment_POST_with_data(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        response = self.client.post(reverse('add_comment', kwargs={'post_id': test_post.id}), {
            'text': 'test description'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(test_post.comments.first().text, 'test description')
        self.assertEqual(self.test_user_1.comments.first().text, 'test description')

    def test_view_add_comment_POST_without_data(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        response = self.client.post(reverse('add_comment', kwargs={'post_id': test_post.id}), {})
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 0)

    # test for delete_comment view
    def test_view_delete_comment_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('delete_comment', kwargs={'id': 1})) 

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/delete_comment'))

    def test_view_delete_comment(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        test_comment = Comment.objects.create(post=test_post, user=self.test_user_1)
        response = self.client.get(reverse('delete_comment', kwargs={'id': test_comment.id})) 

        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Comment.objects.count(), 0)

    # test for thumb_up view
    def test_view_thumb_up_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('thumb_up', kwargs={'id': 1})) 

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/thumb_up'))

    def test_view_thumb_up_with_no_like_under_post(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        response = self.client.get(reverse('thumb_up', kwargs={'id': test_post.id}))
        test_post.refresh_from_db()
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(test_post.likes, 1)
        self.assertEqual(test_post.like_set.first(), self.test_user_1.like_set.first())

    def test_view_thumb_up_with_like_under_post(self):
        test_post = Post.objects.create(user=self.test_user_1, description='test description')
        Like.objects.create(user=self.test_user_1, post=test_post)
        test_post.likes += 1
        test_post.save()

        self.assertEqual(test_post.likes, 1)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(test_post.like_set.first(), self.test_user_1.like_set.first())

        response = self.client.get(reverse('thumb_up', kwargs={'id': test_post.id}))

        test_post.refresh_from_db()
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Like.objects.count(), 0)
        self.assertEqual(test_post.likes, 0)
    
    # test for follow view
    def test_view_follow_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('follow', kwargs={'id': 1})) 

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/follow'))

    def test_view_follow_GET(self):
        response = self.client.get(reverse('follow', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 302)

    def test_view_follow_if_follow_exists(self):
        Follow.objects.create(user=self.test_user_1, user_followed=self.test_user_2, followd_user_id=self.test_user_2.id)
        self.client.get(reverse('follow', kwargs={'id': self.test_user_2.id}))

        self.assertEqual(Follow.objects.count(), 1)

    def test_view_follow_if_follow_not_exists(self):
        self.assertEqual(Follow.objects.count(), 0)
        self.client.get(reverse('follow', kwargs={'id': self.test_user_2.id}))

        self.test_user_1_profile.refresh_from_db()
        self.test_user_2_profile.refresh_from_db()
        
        self.assertEqual(Follow.objects.count(), 1)
        self.assertEqual(self.test_user_1_profile.following_amount, 1)
        self.assertEqual(self.test_user_2_profile.followers_amount, 1)

    # test for unfollow view
    def test_view_unfollow_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('unfollow', kwargs={'id': 1})) 

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/unfollow'))

    def test_view_unfollow_GET(self):
        response = self.client.get(reverse('unfollow', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 302)

    def test_view_unfollow_if_follow_exists(self):
        Follow.objects.create(user=self.test_user_1, user_followed=self.test_user_2, followd_user_id=self.test_user_2.id)
        self.test_user_1_profile.following_amount += 1
        self.test_user_2_profile.followers_amount += 1
        self.test_user_1_profile.save()
        self.test_user_2_profile.save()

        self.assertEqual(Follow.objects.count(), 1)
        self.assertEqual(self.test_user_1_profile.following_amount, 1)
        self.assertEqual(self.test_user_2_profile.followers_amount, 1)

        self.client.get(reverse('unfollow', kwargs={'id': self.test_user_2.id}))

        self.test_user_1_profile.refresh_from_db()
        self.test_user_2_profile.refresh_from_db()

        self.assertEqual(Follow.objects.count(), 0)
        self.assertEqual(self.test_user_1_profile.following_amount, 0)
        self.assertEqual(self.test_user_2_profile.followers_amount, 0)

    def test_view_unfollow_if_follow_not_exists(self):
        # creating the Follow objects by test_user_2 
        Follow.objects.create(user=self.test_user_2, user_followed=self.test_user_1, followd_user_id=self.test_user_1.id)
        self.client.get(reverse('unfollow', kwargs={'id': self.test_user_1.id}))

        self.assertEqual(Follow.objects.count(), 1)

    # test for search view
    def test_view_search_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('search')) 

        self.assertTrue(response.url.startswith('/instagram/login/?next=/instagram/search'))

    def test_view_search_GET_with_correct_data(self):
        response = self.client.get(reverse('search'), {
            'username_search': self.test_user_2.username
        })

        self.assertRedirects(response, f'/instagram/profile/{self.test_user_2_profile.id}')
    
    def test_view_search_GET_with_incorrect_data(self):
        response = self.client.get(reverse('search'))

        self.assertRedirects(response, '/instagram/')