from django.test import TestCase
from base.forms import DepartmentForm, TeacherForm
from base.models import Department, Teacher
from base.forms import StudentForm
from base.forms import CreateUserForm, AdminNoticeForm
from django.contrib.auth.models import User

class DepartmentFormTest(TestCase):
    def test_valid_department_form(self):
        """Test valid DepartmentForm"""
        form_data = {
            'name': 'Test Department',
            'location': 'Block A',
            'rank': 1,
            'phone': '1234567890',
            'email': 'department@example.com',
            'description': 'Test department description'
        }
        form = DepartmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_department_form(self):
        """Test invalid DepartmentForm"""
        form = DepartmentForm(data={})
        self.assertFalse(form.is_valid())

class TeacherFormTest(TestCase):
    def test_valid_teacher_form(self):
        """Test valid TeacherForm"""
        department = Department.objects.create(
            name='Test Department',
            location='Block A',
            rank=1,
            phone='1234567890',
            email='department@example.com',
            description='Test department description'
        )
        form_data = {
            'name': 'Test Teacher',
            'reg_no': '123456',
            'rank': 'Lecturer',
            'dept': department.id,
            'email': 'teacher@example.com',
            'phone': '9876543210',
            'description': 'Test teacher description'
        }
        form = TeacherForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_teacher_form(self):
        """Test invalid TeacherForm"""
        form = TeacherForm(data={})
        self.assertFalse(form.is_valid())



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
