from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post, Comment

# Test
# class SignUpTests(TestCase):
#     username='testuser',        
#     email='test@gmail.com',
#     password='secret'

#     def test_signup_page_url(self):
#         response = self.client.get(reverse('signup'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/signup.html')

#     def test_signup_form(self):
#         self.user = get_user_model().objects.create_user(
#             self.username, self.email, self.password
#         )
#         self.assertEqual(get_user_model().objects.all.count(), 1)
#         self.assertEqual(get_user_model().objects.all.get_user_model()[0].username, self.username)
#         self.assertEqual(get_user_model().objects.all.get_user_model()[0].email, self.email)


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

        self.comment = Comment.objects.create(
            post=self.post,
            comment='Nice comment',
            author=self.user,
        )
    
    def test_string_rep(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)
    
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')
    
    def test_post_content(self):
        self.assertEqual(str(self.post.title), 'A good title')
        self.assertEqual(str(self.post.author), 'testuser')
        self.assertEqual(str(self.post.body), 'Nice body content')
    
    def test_comment_content(self):
        self.assertEqual(str(self.comment.author), 'testuser')
        self.assertEqual(str(self.comment.comment), 'Nice comment')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
    
    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New content',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New content')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated content',
        })
        self.assertEqual(response.status_code, 302)
       
    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
