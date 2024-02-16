from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base import views

class TestUrls(SimpleTestCase):

    def test_create_teacher_url_resolves(self):
        url = reverse('create_teacher')
        self.assertEqual(resolve(url).func, views.create_teacher)
