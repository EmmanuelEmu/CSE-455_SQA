from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base import views

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_common_page_url_resolves(self):
        url = reverse('common_page')
        self.assertEqual(resolve(url).func, views.common_page)

    def test_create_student_url_resolves(self):
        url = reverse('create_student')
        self.assertEqual(resolve(url).func, views.create_student)
