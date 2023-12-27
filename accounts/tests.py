from django.test import TestCase
from django.contrib.auth import get_user_model


class AccountsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='Testuser',
            password='testpass123'
        )

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'login')
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_signup_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'signup')
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(self.user.username, 'Testuser')
        self.assertEqual(get_user_model().objects.all().count(), 1)