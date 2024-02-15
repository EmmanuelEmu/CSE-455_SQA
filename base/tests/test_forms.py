from django.test import TestCase, Client
from base.forms import CreateUserForm


class TestForms(TestCase):
    
    def test_create_user_form_valid_data(self):
        form = CreateUserForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!'
        })
        self.assertTrue(form.is_valid())