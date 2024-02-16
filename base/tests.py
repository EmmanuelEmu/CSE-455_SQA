from django.test import TestCase
from .models import Department
from .forms import DepartmentForm

class DepartmentModelTest(TestCase):
    """
    Tests for the Department model.
    """

    def test_create_department(self):
        """
        Tests that a department can be created successfully.

        This test checks whether a department instance can be created 
        successfully using the DepartmentForm and if the data saved in 
        the database matches the provided input data.
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
        form = DepartmentForm(data)
        self.assertTrue(form.is_valid())
        department = form.save()

        # Assert database fields match expected values
        self.assertEqual(department.name, data['name'])
        self.assertEqual(department.location, data['location'])
        self.assertEqual(department.rank, data['rank'])
        self.assertEqual(department.phone, data['phone'])
        self.assertEqual(department.email, data['email'])
        self.assertEqual(department.description, data['description'])

class DepartmentViewTest(TestCase):
    """
    Tests for the create_department view.
    """

    def test_get_create_department_view(self):
        """
        Tests that the create_department view renders the correct template.

        This test checks whether the create_department view renders the 
        expected template when accessed via HTTP GET request.
        """
        response = self.client.get('/create_department/')
        self.assertEqual(response.status_code, 200)
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
        response = self.client.post('/create_department/', data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/create_department/')  # Replace with your success page
'''

    def test_post_create_department_view_invalid_data(self):
        """
        Tests that the create_department view renders the template with errors on invalid form submission.

        This test checks whether the create_department view correctly renders 
        the template with form errors upon receiving invalid department data 
        via HTTP POST request.
        """
        # Test data for invalid department creation
        data = {'name': ''}  # Missing required field
        response = self.client.post('/create_department/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_department.html')
        self.assertFormError(response, 'form', 'name', 'This field is required.')
'''