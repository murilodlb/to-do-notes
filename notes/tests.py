from django.contrib.auth.models import User
from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteDuplicateSubmitTests(TestCase):
    def setUp(self):
        cache.clear()
        self.user = User.objects.create_user(username="noteuser", password="securepassword123")
        self.client.force_login(self.user)
        self.create_url = reverse("note_create")

    def test_rapid_identical_post_creates_only_one_note(self):
        payload = {"title": "Minha Nota", "body": "Conteúdo da nota"}
        resp1 = self.client.post(self.create_url, payload)
        resp2 = self.client.post(self.create_url, payload)

        self.assertEqual(resp1.status_code, 302)
        self.assertEqual(resp2.status_code, 302)
        self.assertEqual(Note.objects.filter(user=self.user).count(), 1)

    def test_distinct_post_payloads_both_succeed(self):
        resp1 = self.client.post(self.create_url, {"title": "Nota 1", "body": "Texto 1"})
        resp2 = self.client.post(self.create_url, {"title": "Nota 2", "body": "Texto 2"})

        self.assertEqual(resp1.status_code, 302)
        self.assertEqual(resp2.status_code, 302)
        self.assertEqual(Note.objects.filter(user=self.user).count(), 2)

    def test_invalid_post_does_not_lock_subsequent_submission(self):
        invalid_payload = {"title": "", "body": "Sem título"}
        resp1 = self.client.post(self.create_url, invalid_payload)
        resp2 = self.client.post(self.create_url, invalid_payload)

        self.assertEqual(resp1.status_code, 200)
        self.assertEqual(resp2.status_code, 200)
