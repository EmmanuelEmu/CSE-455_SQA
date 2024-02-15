from django.test import TestCase, Client
from django.urls import reverse
from base.forms import AdminNoticeForm  # Make sure to import your form
from base.models import AdminNotice
from django.core.exceptions import ObjectDoesNotExist

class CreateNoticeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_notice_view(self):
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