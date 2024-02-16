from django.test import TestCase, Client
from django.urls import reverse
from base.forms import AdminNoticeForm  # Make sure to import your form
from base.models import AdminNotice
from django.core.exceptions import ObjectDoesNotExist

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

        # Optionally, you can check other details about the response



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
