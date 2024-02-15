from django.test import TestCase
from base.models import Department, Teacher

class DepartmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Department object for testing
        cls.department = Department.objects.create(
            name='Test Department',
            location='Block A',
            rank=1,
            phone='1234567890',
            email='department@example.com',
            description='Test department description'
        )

    def test_department_str_representation(self):
        """Test Department model string representation"""
        self.assertEqual(str(self.department), 'Test Department')

class TeacherModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Department object for testing
        cls.department = Department.objects.create(
            name='Test Department',
            location='Block A',
            rank=1,
            phone='1234567890',
            email='department@example.com',
            description='Test department description'
        )

        # Create a Teacher object for testing
        cls.teacher = Teacher.objects.create(
            name='Test Teacher',
            reg_no='123456',
            rank='Lecturer',
            dept=cls.department,
            email='teacher@example.com',
            phone='9876543210',
            description='Test teacher description'
        )

    def test_teacher_str_representation(self):
        """Test Teacher model string representation"""
        self.assertEqual(str(self.teacher), 'Test Teacher')
