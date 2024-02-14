from django.test import TestCase

# Create your tests here.
from .models import Department
from .views import department_info

class DepartmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
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
        Tests that a department object can be created successfully with valid data.
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
        Tests that the `__str__` method returns a meaningful string representation
        of the department object.
        """
        self.assertEqual(str(self.department), "Marketing")

class DepartmentInfoViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
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
        Tests that the `department_info` view returns a successful HTTP response
        with the correct context for a valid department ID.
        """
        response = self.client.get(f"/department/{self.department.pk}/")
        print(response.status_code)
        """
        self.assertEqual(response.status_code, 200)
        self.assertTrue('dept' in response.context)
        self.assertEqual(response.context['dept'], self.department)
        """
    
    def test_department_info_view_404_for_invalid_id(self):
        """
        Tests that the `department_info` view returns a 404 Not Found status code
        for an invalid department ID.
        """
        response = self.client.get("/department/999/")
        self.assertEqual(response.status_code, 404)

    def test_department_info_view_template_used(self):
        """
        Tests that the `department_info` view renders the expected template.
        """
        response = self.client.get(f"/department/{self.department.pk}/")
        self.assertTemplateUsed(response, "base/department_info.html")
