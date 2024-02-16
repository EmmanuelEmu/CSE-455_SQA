from django.test import TestCase
from base.models import Teacher, Department

class TeacherModelTest(TestCase):
    def setUp(self):
        # Create a Department for testing
        self.department = Department.objects.create(name='Test Department')

        # Create a Teacher instance for testing
        self.teacher = Teacher.objects.create(
            name='Test Teacher',
            reg_no='123456',
            rank='Lecturer',
            dept=self.department,
            email='test@example.com',
            phone='1234567890',
            description='Test description'
        )

    def test_teacher_creation(self):
        """Test Teacher model creation"""
        self.assertTrue(isinstance(self.teacher, Teacher))
        self.assertEqual(self.teacher.name, 'Test Teacher')
        self.assertEqual(self.teacher.reg_no, '123456')
        self.assertEqual(self.teacher.rank, 'Lecturer')
        self.assertEqual(self.teacher.dept, self.department)
        self.assertEqual(self.teacher.email, 'test@example.com')
        self.assertEqual(self.teacher.phone, '1234567890')
        self.assertEqual(self.teacher.description, 'Test description')

    def test_teacher_str_representation(self):
        """Test Teacher model string representation"""
        self.assertEqual(str(self.teacher), 'Test Teacher')
