from django.test import TestCase
from base.forms import CreateUserForm, AdminNoticeForm
from django.contrib.auth.models import User

class CreateUserFormTest(TestCase):
    def test_create_user_form_valid_data(self):
        """
        Test case to check the validity of CreateUserForm with valid data.

        This test checks if the form is valid when provided with valid user data.
        """
        form = CreateUserForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        })
        self.assertTrue(form.is_valid())

    def test_create_user_form_invalid_data(self):
        """
        Test case to check the validity of CreateUserForm with invalid data.

        This test checks if the form is invalid when provided with invalid user data,
        specifically an invalid email format.
        """
        form = CreateUserForm(data={
            'username': 'testuser',
            'email': 'invalidemail',  # Invalid email format
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertFalse(form.is_valid())

class AdminNoticeFormTest(TestCase):
    def test_admin_notice_form_valid_data(self):
        """
        Test case to check the validity of AdminNoticeForm with valid data.

        This test checks if the form is valid when provided with valid notice data.
        """
        form = AdminNoticeForm(data={
            'sender': 'Admin',
            'receiver': 'JohnDoe',
            'subject': 'Test Subject',
            'body': 'Test Body',
        })
        self.assertTrue(form.is_valid())

    def test_admin_notice_form_invalid_data(self):
        """
        Test case to check the validity of AdminNoticeForm with invalid data.

        This test checks if the form is invalid when provided with invalid notice data,
        specifically an empty subject (assuming it's required).
        """
        form = AdminNoticeForm(data={
            'sender': 'Admin',
            'receiver': 'JohnDoe',
            'subject': '',  # Empty subject (assuming it's required)
            'body': 'Test Body',
        })
        self.assertFalse(form.is_valid())
