from django.test import TestCase
from base.forms import StudentForm

class StudentFormTestCase(TestCase):
    """
        Test case to check if the student form is valid with correct data.
        """
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
        """
        Test case to check if the student form is invalid with incorrect data.
        """
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
    

    


    