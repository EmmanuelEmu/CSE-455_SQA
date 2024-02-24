from django.test import TestCase
from base.models import Department

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
