from django.test import TestCase
from base.forms import TeacherForm
from base.models import Teacher, Department

class TeacherFormTest(TestCase):
    def test_teacher_form_valid(self):
        """Test valid form data"""
        department = Department.objects.create(name='Test Department')
        form_data = {
            'name': 'Test Teacher',
            'reg_no': '123456',
            'rank': 'Lecturer',
            'dept': department.id,
            'email': 'test@example.com',
            'phone': '1234567890',
            'description': 'Test description'
        }
        form = TeacherForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_teacher_form_invalid(self):
        """Test invalid form data"""
        form = TeacherForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)  # Assuming there are 6 fields in the form
