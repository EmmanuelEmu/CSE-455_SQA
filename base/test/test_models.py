from django.test import TestCase
from base.models import Department, Teacher
from django.test import TestCase
from base.models import Student
from django.utils import timezone
from base.models import AdminNotice


'''
DepartmentModelTest
===================

Test cases for the Department model.

.. autoclass:: base.tests.DepartmentModelTest
   :members:
   :undoc-members:
   :show-inheritance:

Department Info View Test
=========================

Test cases for the Department info view.

.. autoclass:: base.tests.DepartmentInfoViewTest
   :members:
   :undoc-members:
   :show-inheritance:
'''

class DepartmentModelTest(TestCase):
    """
    Test cases for the Department model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for Department model tests.
        """
        # Create a department object for testing
        cls.department = Department.objects.create(
            name="Marketing",
            location="Block B",
            rank=2,
            phone="555-1234",
            email="marketing@company.com",
            description="Responsible for brand awareness and lead generation.",
        )

    def test_department_creation(self):
        """
        Tests the creation of a department object with valid data.
        """
        # Create a new department object
        department = Department.objects.create(
            name="Sales",
            location="Block B",
            rank=3,
            phone="555-5678",
            email="sales@company.com",
            description="Focuses on closing deals and driving revenue.",
        )
        # Assert that the department object is created correctly
        self.assertEqual(department.name, "Sales")
        self.assertEqual(department.location, "Block B")
        self.assertEqual(department.rank, 3)
        self.assertEqual(department.phone, "555-5678")
        self.assertEqual(department.email, "sales@company.com")
        self.assertTrue(department.description)

    def test_department_string_representation(self):
        """
        Tests the string representation of the department object.
        """
        # Assert that the string representation of the department object is correct
        self.assertEqual(str(self.department), "Marketing")



        
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
        
        

class StudentModelTest(TestCase):
    def test_create_student(self):
        student = Student.objects.create(
            name="Rafi Kibria",
            hsc_roll="12345",
            hsc_reg="ABCD1234",
            reg_no="XYZ12345",
            roll="12301",
            session="2018-2019",
            email="stu@gmail.com",
            phone="0158655554",
            dob='2000-01-01',
            address='123 Main St',
            fathers_name='John Doe Sr.',
            mothers_name='Jane Doe',
            guardian_phone='0987654321',
            description='keep doing hard work ',
            status='Regular',
            CGPA=3.5,
            result_description='Try best until your dreams come true. Best of luck.'
        )

        self.assertEqual(student.name, "Rafi Kibria")
        self.assertEqual(student.hsc_roll, "12345")
        self.assertEqual(student.hsc_reg, "ABCD1234")
        self.assertEqual(student.reg_no, "XYZ12345")
        self.assertEqual(student.roll, "12301")
        self.assertEqual(student.session, "2018-2019")
        self.assertEqual(student.email, "stu@gmail.com")
        self.assertEqual(student.phone, "0158655554")
        self.assertEqual(student.dob, '2000-01-01')        
        self.assertEqual(student.address, '123 Main St')        
        self.assertEqual(student.fathers_name, 'John Doe Sr.')        
        self.assertEqual(student.mothers_name, 'Jane Doe')        
        self.assertEqual(student.guardian_phone, '0987654321')        
        self.assertEqual(student.description, 'keep doing hard work ')        
        self.assertEqual(student.status, 'Regular')        
        self.assertEqual(student.CGPA, 3.5)        
        self.assertEqual(student.result_description, 'Try best until your dreams come true. Best of luck.')


class AdminNoticeModelTest(TestCase):
    def test_admin_notice_creation(self):
        """
        Test case to ensure the creation and behavior of the AdminNotice model.

        This test creates a sample AdminNotice instance, checks the __str__ method,
        and verifies if the fields were saved correctly. It also ensures that the
        date_sent is not in the future.
        """
        # Create a sample AdminNotice instance
        notice = AdminNotice.objects.create(
            sender="Admin",
            receiver="JohnDoe",
            subject="Test Subject",
            body="Test Body",
            date_sent=timezone.now()
        )

        # Check if the __str__ method returns the expected string
        self.assertEqual(str(notice), "Test Subject")

        # Check if the fields were saved correctly
        self.assertEqual(notice.sender, "Admin")
        self.assertEqual(notice.receiver, "JohnDoe")
        self.assertEqual(notice.subject, "Test Subject")
        self.assertEqual(notice.body, "Test Body")

        # Check if the date_sent is not in the future
        self.assertLessEqual(notice.date_sent, timezone.now())

