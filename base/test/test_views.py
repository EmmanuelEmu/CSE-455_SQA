from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from base.models import Teacher
from django.contrib.auth.models import User
from base.views import update_teacher

class TeacherInfoViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.teacher = Teacher.objects.create(name='Test Teacher')

    def test_teacher_info_view(self):
        response = self.client.get(reverse('teacher_info', args=[self.teacher.pk]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/teacher_info.html')
        self.assertEqual(response.context['teacher'], self.teacher)


class TeacherUpdateTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.teacher = Teacher.objects.create(name='John Doe', email='john@example.com')  # Create a sample teacher

    def test_update_teacher(self):
        url = reverse('update_teacher', args=(self.teacher.pk,))
        data = {'name': 'Jane Doe', 'email': 'jane@example.com'}
        request = self.factory.post(url, data)
        response = update_teacher(request, pk=self.teacher.pk)
        self.assertEqual(response.status_code, 302)  # Check if redirected after successful form submission
        updated_teacher = Teacher.objects.get(pk=self.teacher.pk)
        self.assertEqual(updated_teacher.name, 'Jane Doe')  # Check if name is updated correctly
        self.assertEqual(updated_teacher.email, 'jane@example.com')  # Check if email is updated correctly

        # Additional tests if needed

    def test_update_teacher_invalid_form(self):
        url = reverse('update_teacher', args=(self.teacher.pk,))
        data = {'name': '', 'email': 'jane@example.com'}  # Invalid form data
        request = self.factory.post(url, data)
        response = update_teacher(request, pk=self.teacher.pk)
        self.assertEqual(response.status_code, 200)  # Check if form is re-rendered
        # self.assertContains(response, 'This field is required.')  # Check if form errors are displayed
