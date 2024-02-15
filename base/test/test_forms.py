from django.test import TestCase
from base.forms import DepartmentForm, TeacherForm
from base.models import Department, Teacher

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
