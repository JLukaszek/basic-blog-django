from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth import get_user_model


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='Testuser',
            password='testpass123'
        )

    def setUp(self):
        self.post = Post.objects.create(
            title='New title',
            slug='new-title',
            author=self.user,
            body='New body',
        )

    def test_homepage(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'All posts:')
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_create_view(self):
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.title, 'New title')
        self.assertEqual(self.post.body, 'New body')
        self.assertEqual(self.post.author, self.user)

    def test_detail_view(self):
        response = self.client.get('/post/1/detail/')
        noresponse = self.client.get('/post/11111111/detail/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(noresponse.status_code, 404)
        self.assertEqual(self.post.title, 'New title')
        self.assertEqual(self.post.body, 'New body')
        self.assertEqual(self.post.author, self.user)
        self.assertContains(response, 'New title')
        self.assertTemplateUsed(response, 'blog/post_detail.html')
