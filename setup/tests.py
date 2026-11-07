from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .forms import SignUpForm


class SignUpViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse("signup")

    def test_signup_form_valid(self):
        form = SignUpForm(data={
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "ComplexPass123!@",
            "password2": "ComplexPass123!@",
        })
        self.assertTrue(form.is_valid(), form.errors)
        user = form.save()
        self.assertEqual(user.username, "newuser")
        self.assertEqual(user.email, "newuser@example.com")

    def test_signup_form_requires_email(self):
        form = SignUpForm(data={
            "username": "newuser",
            "email": "",
            "password1": "ComplexPass123!@",
            "password2": "ComplexPass123!@",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_signup_invalid_password_creates_single_consolidated_message(self):
        # Submitting simple short password triggering multiple password validators
        response = self.client.post(self.signup_url, {
            "username": "testuser1",
            "email": "test@example.com",
            "password1": "123",
            "password2": "123",
        })
        self.assertEqual(response.status_code, 200)

        # Retrieve messages stored in request
        messages = list(get_messages(response.wsgi_request))
        # Should be exactly 1 consolidated alert message
        self.assertEqual(len(messages), 1)
        alert_content = str(messages[0])
        self.assertIn("Erros no cadastro:", alert_content)

        # Fields username and email should be preserved in response HTML
        self.assertContains(response, 'value="testuser1"')
        self.assertContains(response, 'value="test@example.com"')
