from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base import views

class TestUrls(SimpleTestCase):
    """
        Test case to verify that the 'home' URL resolves to the correct view function.
    """

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_common_page_url_resolves(self):
        """
        Test case to verify that the 'common_page' URL resolves to the correct view function.
        """
        url = reverse('common_page')
        self.assertEqual(resolve(url).func, views.common_page)

    def test_create_student_url_resolves(self):
        """
        Test case to verify that the 'create_student' URL resolves to the correct view function.
        """
        url = reverse('create_student')
        self.assertEqual(resolve(url).func, views.create_student)

    def test_student_info_url_resolves(self):
        """
        Test case to verify that the 'student_info' URL with an argument resolves to the correct view function.
        """
        url = reverse('student_info', args=['1']) 
        self.assertEqual(resolve(url).func, views.studentinfo)

    def test_update_student_url_resolves(self):
        """
        Test if the update_student URL resolves correctly.
        """
        url = reverse('update_student', kwargs={'pk': '1'})
        self.assertEqual(url, '/update_student/1/')