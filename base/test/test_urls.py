from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base import views
from django.test import TestCase

class TestUrls(SimpleTestCase):
    
    def test_teacher_info_url_resolves(self):
        url = reverse('teacher_info', args=['some_teacher_id'])
        self.assertEqual(resolve(url).func, views.teacher_info)

    def test_create_department_url_resolves(self):
        url = reverse('create_department')
        self.assertEqual(resolve(url).func, views.create_department)
class TestUpdateTeacherURL(TestCase):
    def test_update_teacher_url_resolves(self):
        # Define the URL with a sample primary key
        url = reverse('update_teacher', kwargs={'pk': 'sample_pk'})

        # Use resolve to get the resolved view function
        resolved_view = resolve(url)

        # Assert that the resolved view function matches the expected view function
        self.assertEqual(resolved_view.func, views.update_teacher)

        # Assert that the 'pk' parameter is passed correctly to the view function
        self.assertEqual(resolved_view.kwargs['pk'], 'sample_pk')