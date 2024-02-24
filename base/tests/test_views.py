from django.test import TestCase, Client
from django.urls import reverse
from base.forms import AdminNoticeForm  # Make sure to import your form
from base.models import AdminNotice
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

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







class CreateNoticeViewTest(TestCase):
    """
    Test case for the 'create_notice' view in the 'base' app.

    This test case checks the behavior of the 'create_notice' view with valid and invalid form data.
    """
    def setUp(self):
        """
        Set up necessary data for the test case.
        """
        self.client = Client()

    def test_create_notice_view(self):
        """
        Test the 'create_notice' view with valid form data.

        This test makes a POST request with valid form data, checks if the response redirects to the 'home' page,
        and verifies that a notice was created in the database.
        """
        # Define the URL for the create_notice view
        url = reverse('create_notice')

        # Make a POST request with valid form data
        data = {
            'sender': 'Admin',
            'receiver': 'JohnDoe',
            'subject': 'Test Subject',
            'body': 'Test Body',
        }
        response = self.client.post(url, data)

        # Check if the response redirects to the 'home' page
        self.assertRedirects(response, reverse('home'))

        # Check if a notice was created in the database
        self.assertEqual(AdminNotice.objects.count(), 1)

        # Optionally, you can check other details about the created notice

    def test_create_notice_view_invalid_form(self):
        """
        Test the 'create_notice' view with invalid form data.

        This test makes a POST request with invalid form data, checks if the response renders the 'create_notice' template,
        and ensures that the form in the context is an instance of AdminNoticeForm.
        """
        # Define the URL for the create_notice view
        url = reverse('create_notice')

        # Make a POST request with invalid form data
        data = {
            # Missing required fields
        }
        response = self.client.post(url, data)

        # Check if the response renders the create_notice template
        self.assertTemplateUsed(response, 'base/create_notice.html')

        # Check if the form in the context is an instance of AdminNoticeForm
        self.assertIsInstance(response.context['form'], AdminNoticeForm)

        # Check if the notice count in the database remains unchanged
        self.assertEqual(AdminNotice.objects.count(), 0)


# class UpdateNoticeViewTest(TestCase):
#     """
#     Test case for the 'create_notice' view in the 'base' app.

#     This test case checks the behavior of the 'create_notice' view with valid and invalid form data.
#     """
#     def setUp(self):
#         """
#         Set up necessary data for the test case.
#         """
#         self.client = Client()

#     def test_update_notice_view(self):
#         """
#         Test the 'create_notice' view with valid form data.

#         This test makes a POST request with valid form data, checks if the response redirects to the 'home' page,
#         and verifies that a notice was created in the database.
#         """
#         # Define the URL for the create_notice view
#         url = reverse('create_notice')

#         # Make a POST request with valid form data
#         data = {
#             'sender': 'Admin',
#             'receiver': 'JohnDoe',
#             'subject': 'Test Subject',
#             'body': 'Test Body',
#         }
#         response = self.client.post(url, data)

#         # Check if the response redirects to the 'home' page
#         self.assertRedirects(response, reverse('home'))

#         # Check if a notice was created in the database
#         self.assertEqual(AdminNotice.objects.count(), 1)

#         # Optionally, you can check other details about the created notice

#     def test_update_notice_view_invalid_form(self):
#         """
#         Test the 'create_notice' view with invalid form data.

#         This test makes a POST request with invalid form data, checks if the response renders the 'create_notice' template,
#         and ensures that the form in the context is an instance of AdminNoticeForm.
#         """
#         # Define the URL for the create_notice view
#         url = reverse('create_notice')

#         # Make a POST request with invalid form data
#         data = {
#             # Missing required fields
#         }
#         response = self.client.post(url, data)

#         # Check if the response renders the create_notice template
#         self.assertTemplateUsed(response, 'base/create_notice.html')

#         # Check if the form in the context is an instance of AdminNoticeForm
#         self.assertIsInstance(response.context['form'], AdminNoticeForm)

#         # Check if the notice count in the database remains unchanged
#         self.assertEqual(AdminNotice.objects.count(), 0)





class AdminNoticeViewTests(TestCase):
    def setUp(self):
        # Create a test user (optional)
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test notice
        self.notice = AdminNotice.objects.create(sender='Admin', receiver='Sizan')

    def test_update_notice_view_get(self):
        """
        Test that the update_notice view returns a form for updating an existing notice (GET request).
        """
        self.client.login(username='testuser', password='testpassword')  # If authentication is required
        url = reverse('update_notice', args=[self.notice.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_notice.html')
        self.assertIsInstance(response.context['form'], AdminNoticeForm)
        self.assertEqual(response.context['form'].instance, self.notice)

    


class NoticeDetailsViewTest(TestCase):
    """
    Test case for the 'notice_details' view in the 'base' app.

    This test case checks the behavior of the 'notice_details' view with valid and invalid notice IDs.
    """
    def setUp(self):
        """
        Set up necessary data for the test case.
        """
        # Create a sample notice for testing
        self.notice = AdminNotice.objects.create(
            sender="Admin",
            receiver="JohnDoe",
            subject="Test Subject",
            body="Test Body",
        )
        self.client = Client()

    def test_notice_details_view(self):
        """
        Test the 'notice_details' view with a valid notice ID.

        This test makes a GET request to the 'notice_details' view, checks if the response is as expected,
        and verifies that the notice in the context matches the created notice.
        """
        # Define the URL for the notice_details view with the notice's ID
        url = reverse('notice_details', args=[self.notice.id])

        # Make a GET request to the notice_details view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered template is 'base/notice_details.html'
        self.assertTemplateUsed(response, 'base/notice_details.html')

        # Check if the notice in the context matches the created notice
        self.assertEqual(response.context['notice'], self.notice)

    def test_notice_details_view_invalid_id(self):
        """
        Test the 'notice_details' view with an invalid notice ID.

        This test makes a GET request to the 'notice_details' view with an invalid ID and expects an exception.
        """
    # Define an invalid notice ID
        invalid_id = 999

    # Define the URL for the notice_details view with the invalid ID
        url = reverse('notice_details', args=[invalid_id])

    # Make a GET request to the notice_details view with an invalid ID
        with self.assertRaises(AdminNotice.DoesNotExist):
            self.client.get(url)

    # No need to access the response variable here, as it's not expected to be defined

class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        """
        Test if the home view returns a status code of 200 (OK).
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        """
        Test if the home view uses the correct template.
        """
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base/home.html')