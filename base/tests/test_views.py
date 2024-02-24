from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from base.forms import CreateUserForm
from django.http import HttpRequest
from base.models import Student
from base.forms import StudentForm
from django.core.exceptions import ObjectDoesNotExist
from base.views import create_student




class NavStuListTest(TestCase):
    """
    Test case for the nav_stu_list.

    Inherits from:
    - TestCase: Django's built-in test case class.

    Attributes:
    - student1: Sample instance of the Student model for testing.
    - student2: Sample instance of the Student model for testing.
    - student3: Sample instance of the Student model for testing.

    Methods:
    - setUp: Method to set up sample data for testing.
    - test_nav_stu_list_view: Method to test the functionality of the nav_stu_list view.

    Usage:
    This test case is designed to test the functionality of the nav_stu_list view including basic rendering
    and filtering.


    Django Models:
    - Student: The Django model representing student information.

    Dependencies:
    - Django must be properly installed in the project.
    - TestCase class should be imported from 'django.test'.
    - Client class and reverse function should be imported from 'django.test.client'.
    - Student model should be imported from the appropriate module.


    Notes:
    The test case sets up sample data with three student instances and tests the rendering and filtering
    functionality of the NavStuList view using Django's test client.

    """
    def setUp(self):
        """
        Set up sample data for testing.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Create some sample data for testing
        self.student1 = Student.objects.create(
            name="John", roll="001", CGPA=3.7, status='Regular'
        )
        self.student2 = Student.objects.create(
            name="Jane", roll="002", CGPA=3.0, status='Ex-Student'
        )
        self.student3 = Student.objects.create(
            name="Smith", roll="003", CGPA=3.8, status='Regular'
        )

    def test_nav_stu_list_view(self):
        """
        Test the functionality of the nav_stu_list view.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Create a client for making requests
        client = Client()

        # Make a GET request to the view
        response = client.get(reverse('nav_stu_list'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered HTML contains the names of the students
        self.assertContains(response, 'John')
        self.assertContains(response, 'Jane')
        self.assertContains(response, 'Smith')

        # Test the filtering by providing query parameters in the request
        response_filtered = client.get(reverse('nav_stu_list'), {'status': 'Regular'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response_filtered.status_code, 200)

        # Check if the rendered HTML contains the filtered students
        self.assertContains(response_filtered, 'John')
        self.assertNotContains(response_filtered, 'Jane')
        self.assertContains(response_filtered, 'Smith')







class DeleteStudentTest(TestCase):
    """
    Test case for the delete_student.

    Inherits:
    - TestCase: Django's built-in test case class.

    Attributes:
    - student1: Sample instance of the Student model for testing.

    Methods:
    - setUp: Method to set up sample data for testing.
    - test_delete_student_view: Method to test the functionality of the DeleteStudent view.

    Usage:
    This test case is designed to test the functionality of the DeleteStudent view, including rendering
    and the deletion of a student.

   
    Django Models:
    - Student: The Django model representing student information.

    Dependencies:
    - Django must be properly installed in the project.
    - TestCase class should be imported from 'django.test'.
    - Client class and reverse function should be imported from 'django.test.client'.



    Notes:
    The test case sets up sample data with one student instance and tests the rendering and deletion
    functionality of the delete_student view using Django's test client.

    """
    def setUp(self):
        """
        Set up sample data for testing.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Create some sample data for testing
        self.student1 = Student.objects.create(
            name="John", roll="001", status='Regular'
        )

    def test_delete_student_view(self):
        """
        Test the functionality of the delete_student view.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Create a client for making requests
        client = Client()

        # Get the URL for deleting the student
        url = reverse('delete_student', args=[self.student1.id])

        # Make a GET request to the view
        response = client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered HTML contains the student's information
        self.assertContains(response, 'John')

        # Make a POST request to delete the student
        response_post = client.post(url)

        # Check if the response redirects to 'home'
        self.assertRedirects(response_post, reverse('home'))

        # Check if the student is deleted
        self.assertEqual(Student.objects.count(), 0)









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










