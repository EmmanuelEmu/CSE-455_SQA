from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base import views

class TestUrls(SimpleTestCase):
    
    def test_teacher_info_url_resolves(self):
        url = reverse('teacher_info', args=['some_teacher_id'])
        self.assertEqual(resolve(url).func, views.teacher_info)

    def test_create_department_url_resolves(self):
        url = reverse('create_department')
        self.assertEqual(resolve(url).func, views.create_department)
