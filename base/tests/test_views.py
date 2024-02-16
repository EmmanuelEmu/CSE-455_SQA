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
    """
    Test case for the common_page view.

    Methods:
    - setUp(): Set up necessary variables for testing.
    - test_common_page_view(): Test the common_page view.
    """

    def setUp(self):
        """
        Set up necessary variables for testing.

        Creates a test client and defines the common_page URL.
        """
        self.client = Client()
        self.common_page_url = reverse('common_page') 

    def test_common_page_view(self):
        """
        Test the common_page view.

        Simulates a GET request to the common_page view and asserts the response status code and template used.
        """
        response = self.client.get(self.common_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/common_page.html')


class TestRegister(TestCase):
    """
    Test case for the register view.

    Methods:
    - setUp(): Set up necessary variables for testing.
    - test_register_view_get(): Test the GET request to the register view.
    - test_register_view_post_valid_form(): Test the POST request to the register view with a valid form.
    """

    def setUp(self):
        """
        Set up necessary variables for testing.

        Creates a test client and defines the register and login URLs.
        """
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_register_view_get(self):
        """
        Test the GET request to the register view.

        Simulates a GET request to the register view and asserts the response status code and template used.
        """
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register.html')

    def test_register_view_post_valid_form(self):
        """
        Test the POST request to the register view with a valid form.

        Simulates a POST request to the register view with valid form data and asserts the redirection to the login page.
        """
        form_data = {
            'username': 'testuser',
            'email':'email@gmail.com',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!'
        }
        response = self.client.post(self.register_url, data=form_data)
        self.assertRedirects(response, self.login_url)


class TestLoginAdmin(TestCase):
    """
    Test case for the login_admin view.

    Methods:
    - setUp(): Set up necessary variables for testing.
    - test_login_admin_view_incorrect_credentials(): Test the login_admin view with incorrect credentials.
    - test_login_admin_view_correct_credentials(): Test the login_admin view with correct credentials.
    """

    def setUp(self):
        """
        Set up necessary variables for testing.

        Creates a test user for login attempts.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_admin_view_incorrect_credentials(self):
        """
        Test the login_admin view with incorrect credentials.

        Simulates a login attempt with incorrect credentials and asserts the response status code and error message.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('login'), {
            'username': 'incorrect_user',
            'password': 'incorrect_password'
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username or Password is incorrect")

    def test_login_admin_view_correct_credentials(self):
        """
        Test the login_admin view with correct credentials.

        Simulates a login attempt with correct credentials and asserts the successful redirection to the home page.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('home')))


class TestLogoutAdmin(TestCase):
    """
    Test case for the logout_user view.

    Methods:
    - test_logout_user_view(): Test the logout_user view.
    """

    def test_logout_user_view(self):
        """
        Test the logout_user view.

        Simulates a GET request to the logout_user view and asserts the response status code.
        """
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)