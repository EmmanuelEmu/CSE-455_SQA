from django.test import TestCase
<<<<<<< HEAD
from base.forms import StudentForm

class StudentFormTestCase(TestCase):
    def test_student_form_valid(self):
        form_data = {
            'name': 'John Doe',
            'hsc_roll': '123456',
            'hsc_reg': '7890123456',
            'reg_no': 'ABCDE1234',
            'roll': 'A12345',
            'session': '2022-2023',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'dob': '1990-01-01',
            'address': '123 Main St, City',
            'fathers_name': 'Michael Doe',
            'mothers_name': 'Jane Doe',
            'guardian_phone': '9876543210',
            'description': 'Lorem ipsum dolor sit amet',
            'status': 'Regular',
            'CGPA': '3.5',
            'result_description': 'Lorem ipsum dolor sit amet'
        }

        form = StudentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_student_form_invalid(self):
        form_data = {
            'name': 'John Doe',
            'hsc_roll': '123456',
            'hsc_reg': '7890123456',
            'reg_no': 'ABCDE1234',
            'roll': 'A12345',
            'session': '2022-2023',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'dob': '1990-01-01',
            'address': '123 Main St, City',
            'fathers_name': 'Michael Doe',
            'mothers_name': 'Jane Doe',
            'guardian_phone': '9876543210',
            'description': 'Lorem ipsum dolor sit amet',
            'status': 'Regular',
            'CGPA': '5.0',  
            'result_description': 'Lorem ipsum dolor sit amet'
        }

        form = StudentForm(data=form_data)
        self.assertFalse(form.is_valid())
    

    


    
=======
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
>>>>>>> notice_details
