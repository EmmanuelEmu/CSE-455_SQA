from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from base.forms import CreateUserForm
from django.http import HttpRequest
from base.models import Student
from base.forms import StudentForm
from django.core.exceptions import ObjectDoesNotExist
from base.views import create_student

class TestCommonPageView(TestCase):

    def setUp(self):
        self.client = Client()
        # Replace 'common_page' with  actual URL name
        self.common_page_url = reverse('common_page') 
        

    def test_common_page_view(self):
        # Simulate a GET request to the common_page view
        response = self.client.get(self.common_page_url)

        # Assert that the response status code is 200, indicating success
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is being used to render the response
        self.assertTemplateUsed(response, 'base/common_page.html')


class TestRegisterView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')  # Replace 'register' with  actual URL name
        self.login_url = reverse('login')  # Replace 'login' with actual URL name

    def test_register_view_get(self):
        # Simulate a GET request to the register view
        response = self.client.get(self.register_url)

        # Assert that the response status code is 200, indicating success
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is being used to render the response
        self.assertTemplateUsed(response, 'base/register.html')

       

    def test_register_view_post_valid_form(self):
        # Simulate a POST request to the register view with a valid form submission
        form_data = {
            'username': 'testuser',
            'email':'email@gmail.com',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!'
        }
        response = self.client.post(self.register_url, data=form_data)

        # Assert that the response redirects to the login page upon successful registration
        self.assertRedirects(response, self.login_url)

       








class TestLoginAdminView(TestCase):

    def setUp(self):
        # Create a test user for the correct login attempt
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_admin_view_incorrect_credentials(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Test login functionality with incorrect credentials
        response = self.client.post(reverse('login'), {
            'username': 'incorrect_user',
            'password': 'incorrect_password'
        })

        self.assertEqual(response.status_code, 200)

        # Assert that the error message is present in the response content
        self.assertContains(response, "Username or Password is incorrect")


    def test_login_admin_view_correct_credentials(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Test login functionality with correct credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Assert that the login attempt was successful and redirected to the home page (status code 302)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('home')))

        




class TestLogoutAdminView(TestCase):

    def test_logout_user_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

