from django.test import TestCase, Client
from base.forms import CreateUserForm





class TestForms(TestCase):
    """
    Test case for form validation.

    Inherits from:
    - TestCase: Django's built-in test case class.

    Methods:
    - test_create_user_form_valid_data: Method to test the validation of CreateUserForm with valid data.

    Usage:
    This test case is designed to test the validation of forms focusing on the CreateUserForm.

    

    Dependencies:
    - Django must be properly installed in the project.
    - TestCase class should be imported from 'django.test'.
    - CreateUserForm class should be imported from the appropriate module.

    Notes:
    The test case includes a method to test the validation of CreateUserForm with valid data.

    """
    def test_create_user_form_valid_data(self):
        """
        Test the validation of CreateUserForm with valid data.

        """
        # Create an instance of CreateUserForm with valid data
        form = CreateUserForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!'
        })

        # Assert that the form is valid
        self.assertTrue(form.is_valid())