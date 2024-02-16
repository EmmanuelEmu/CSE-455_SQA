from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse
from base.forms import TeacherForm  # Import your TeacherForm
from base.models import Teacher  # Import your Teacher model
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirectBase
from django.http import HttpResponseRedirect

class CreateTeacherViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_teacher_url = reverse('create_teacher')  # Assuming 'create_teacher' is the name of your URL pattern
        self.home_url = reverse('home')
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_teacher_post(self):
        # Assuming valid form data
        form_data = {
            'name': 'Test Teacher',
            'reg_no': '123456',
            'rank': 'Lecturer',
            'dept': '',  # Pass an empty string for the dept field
            'email': 'test@example.com',
            'phone': '1234567890',
            'description': 'Test description'
        }

        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.create_teacher_url, form_data)

        # Check if the teacher was created successfully and redirected to 'home'
        self.assertEqual(response.status_code, 302)  # 302 is the status code for redirect
        self.assertEqual(response.url, reverse('home'))  # Assuming 'home' is the name of your home URL pattern
        # self.assertRedirects(response, self.home_url)
        self.assertTrue(Teacher.objects.filter(name='Test Teacher').exists())
    


    def test_create_teacher_invalid_form(self):
        # Assuming invalid form data
        invalid_form_data = {
            'name': 'Test Teacher',
            'reg_no': '123456',
            'rank': 'Lecturer',
            'dept': '',  # Pass an empty string for the dept field
            'email': 'test@example.com',
            'phone': '1234567890',
            'description': 'Test description'
        }

        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.create_teacher_url, invalid_form_data)

        # Check if the form is re-rendered with errors
        self.assertEqual(response.status_code, 200)  # 200 is the status code for successful HTTP response
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'subject', 'This field is required.')
        # Add more assertions for other fields as necessary

    def test_create_teacher_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.create_teacher_url)

        # Check if the response is successful and the correct template is rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_teacher.html')
from base.models import Teacher

class TeacherInfoViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.teacher = Teacher.objects.create(name='Test Teacher')

    def test_teacher_info_view(self):
        response = self.client.get(reverse('teacher_info', args=[self.teacher.pk]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/teacher_info.html')
        self.assertEqual(response.context['teacher'], self.teacher)
