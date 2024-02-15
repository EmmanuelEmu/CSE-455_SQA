from django.test import TestCase
from base.forms import CreateUserForm, AdminNoticeForm
from django.contrib.auth.models import User

class CreateUserFormTest(TestCase):
    def test_create_user_form_valid_data(self):
        form = CreateUserForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        })
        self.assertTrue(form.is_valid())

    def test_create_user_form_invalid_data(self):
        form = CreateUserForm(data={
            'username': 'testuser',
            'email': 'invalidemail',  # Invalid email format
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertFalse(form.is_valid())

class AdminNoticeFormTest(TestCase):
    def test_admin_notice_form_valid_data(self):
        form = AdminNoticeForm(data={
            'sender': 'Admin',
            'receiver': 'JohnDoe',
            'subject': 'Test Subject',
            'body': 'Test Body',
        })
        self.assertTrue(form.is_valid())

    def test_admin_notice_form_invalid_data(self):
        form = AdminNoticeForm(data={
            'sender': 'Admin',
            'receiver': 'JohnDoe',
            'subject': '',  # Empty subject (assuming it's required)
            'body': 'Test Body',
        })
        self.assertFalse(form.is_valid())
