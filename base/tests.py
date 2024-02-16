from django.test import TestCase
from .models import Department
from .views import department_info

'''
DepartmentModelTest
===================

Test cases for the Department model.

.. autoclass:: myapp.tests.DepartmentModelTest
   :members:
   :undoc-members:
   :show-inheritance:

Department Info View Test
=========================

Test cases for the Department info view.

.. autoclass:: myapp.tests.DepartmentInfoViewTest
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
        department = Department.objects.create(
            name="Sales",
            location="Block B",
            rank=3,
            phone="555-5678",
            email="sales@company.com",
            description="Focuses on closing deals and driving revenue.",
        )
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
        self.assertEqual(str(self.department), "Marketing")

class DepartmentInfoViewTest(TestCase):
    """
    Test cases for the Department info view.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for Department info view tests.
        """
        cls.department = Department.objects.create(
            name="IT",
            location="Block D",
            rank=1,
            phone="555-9012",
            email="it@company.com",
            description="Provides technical support and infrastructure.",
        )

    def test_department_info_view_successful_response(self):
        """
        Tests that the department info view returns a successful HTTP response
        with the correct context for a valid department ID.
        """
        response = self.client.get(f"/department_info/{self.department.pk}/")
      
        self.assertEqual(response.status_code, 200)
        self.assertTrue('dept' in response.context)
        self.assertEqual(response.context['dept'], self.department)
    
    
    def test_department_info_view_404_for_invalid_id(self):
        """
        Tests that the department info view returns a 404 Not Found status code
        for an invalid department ID.
        """
        response = self.client.get("/department/999/")
        self.assertEqual(response.status_code, 404)

    def test_department_info_view_template_used(self):
        """
        Tests that the department info view renders the expected template.
        """
        response = self.client.get(f"/department_info/{self.department.pk}/")
        self.assertTemplateUsed(response, "base/department_info.html")
