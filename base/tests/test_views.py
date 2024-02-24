from base.views import department_info
from base.models import Department
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from base.views import update_department
from base.forms import DepartmentForm
from django.urls import reverse





'''
.. module:: base.tests
   :synopsis: Tests for base.

DepartmentViewTest
------------------

.. autoclass:: base.tests.DepartmentViewTest
   :members:
   :undoc-members:
   :show-inheritance:

   Tests for the create_department view.

   This class contains test cases for the create_department view.

   .. automethod:: test_get_create_department_view
   .. automethod:: test_post_create_department_view_valid_data

   .. note::
      Replace '/create_department/' with the appropriate URL patterns in your application.
      Adjust the expected redirect URL in the second test case accordingly.

   .. note::
      You may need to import necessary modules and set up your test environment accordingly.

'''

class DepartmentViewTest(TestCase):
    """
    Tests for the create_department view.
    
    This class contains test cases for the create_department view.
    """

    def test_get_create_department_view(self):
        """
        Tests that the create_department view renders the correct template.

        This test checks whether the create_department view renders the 
        expected template when accessed via HTTP GET request.
        """
        # Send a GET request to the create_department view
        response = self.client.get('/create_department/')
        
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'base/create_department.html')

    def test_post_create_department_view_valid_data(self):
        """
        Tests that the create_department view redirects to the success page on valid form submission.

        This test verifies that upon submitting a valid department creation 
        form via HTTP POST request, the create_department view redirects 
        the user to the success page.
        """
        # Test data for department creation
        data = {
            'name': 'Test Department',
            'location': 'Block A',
            'rank': 1,
            'phone': '123-456-7890',
            'email': 'test@example.com',
            'description': 'A test department for testing purposes.',
        }
        
        # Send a POST request with valid form data to the create_department view
        response = self.client.post('/create_department/', data)
        
        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        
        # Assert that the response redirects to the expected URL (replace with your success page)
        self.assertRedirects(response, '/create_department/')


'''

DepartmentInfoViewTest
-----------------------

Test cases for the Department info view.

.. automodule:: base.tests
   :members:
   :undoc-members:
   :show-inheritance:

    DepartmentInfoViewTest.setUpTestData
    ------------------------------------

    Set up test data for Department info view tests.

    .. code-block:: python

        def setUpTestData(cls):
            cls.department = Department.objects.create(
                name="IT",
                location="Block D",
                rank=1,
                phone="555-9012",
                email="it@company.com",
                description="Provides technical support and infrastructure.",
            )

    DepartmentInfoViewTest.test_department_info_view_successful_response
    ----------------------------------------------------------------------

    Tests that the department info view returns a successful HTTP response
    with the correct context for a valid department ID.

    .. code-block:: python

        def test_department_info_view_successful_response(self):
            response = self.client.get(f"/department_info/{self.department.pk}/")
            self.assertEqual(response.status_code, 200)
            self.assertTrue('dept' in response.context)
            self.assertEqual(response.context['dept'], self.department)

    DepartmentInfoViewTest.test_department_info_view_404_for_invalid_id
    ---------------------------------------------------------------------

    Tests that the department info view returns a 404 Not Found status code
    for an invalid department ID.

    .. code-block:: python

        def test_department_info_view_404_for_invalid_id(self):
            response = self.client.get("/department/999/")
            self.assertEqual(response.status_code, 404)

    DepartmentInfoViewTest.test_department_info_view_template_used
    ---------------------------------------------------------------------

    Tests that the department info view renders the expected template.

    .. code-block:: python

        def test_department_info_view_template_used(self):
            response = self.client.get(f"/department_info/{self.department.pk}/")
            self.assertTemplateUsed(response, "base/department_info.html")
'''



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
        # Make a GET request to the department_info view using the department's primary key
        response = self.client.get(f"/department_info/{self.department.pk}/")
      
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the 'dept' object is present in the response context
        self.assertTrue('dept' in response.context)
        # Assert that the 'dept' object in the context matches the created department
        self.assertEqual(response.context['dept'], self.department)
    
    
    def test_department_info_view_404_for_invalid_id(self):
        """
        Tests that the department info view returns a 404 Not Found status code
        for an invalid department ID.
        """
        # Make a GET request to a non-existent department ID
        response = self.client.get("/department/999/")
        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

    def test_department_info_view_template_used(self):
        """
        Tests that the department info view renders the expected template.
        """
        # Make a GET request to the department_info view using the department's primary key
        response = self.client.get(f"/department_info/{self.department.pk}/")
        # Assert that the response uses the expected template
        self.assertTemplateUsed(response, "base/department_info.html")








"""
.. module:: base.tests
   :synopsis: Tests for the base app.

DepartmentUpdateViewTests
-------------------------

Tests for the Department update view.

.. autoclass:: base.tests.DepartmentUpdateViewTests
   :members:

   TestCase for testing the Department update view.

   .. automethod:: setUp

   .. automethod:: test_update_department_get

   .. automethod:: test_update_department_post_invalid

   .. automethod:: test_update_department_post_valid
"""



class DepartmentUpdateViewTests(TestCase):
    """
    TestCase for testing the Department update view.

    """
    def setUp(self):
        """
        Set up initial data for the tests.

        """
        self.client = Client()
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.client.force_login(self.user)
        self.department = Department.objects.create(name='Test Department', location='Block A', rank=1, phone='1234567890', email='test@example.com', description='Test Description')

    def test_update_department_get(self):
        """
        Test the GET request to update a department.

        """
        url = reverse('update_department', kwargs={'pk': self.department.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], DepartmentForm)

    def test_update_department_post_invalid(self):
        """
        Test the POST request with invalid data to update a department.

        """
        url = reverse('update_department', kwargs={'pk': self.department.pk})
        invalid_data = {
            'name': '',  # Name field is required, providing empty string here
            'location': 'Block A',
            'rank': 2,
            'phone': '1234567890',
            'email': 'test@example.com',
            'description': 'Test Description'
        }
        response = self.client.post(url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())  # Form should be invalid

    def test_update_department_post_valid(self):
        """
        Test the POST request with valid data to update a department.

        """
        url = reverse('update_department', kwargs={'pk': self.department.pk})
        valid_data = {
            'name': 'Updated Department',
            'location': 'Block B',
            'rank': 2,
            'phone': '1234567890',
            'email': 'test@example.com',
            'description': 'Updated Description'
        }
        response = self.client.post(url, data=valid_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        updated_department = Department.objects.get(pk=self.department.pk)
        self.assertEqual(updated_department.name, 'Updated Department')
        self.assertEqual(updated_department.location, 'Block B')
        self.assertEqual(updated_department.rank, 2)
        self.assertEqual(updated_department.description, 'Updated Description')


