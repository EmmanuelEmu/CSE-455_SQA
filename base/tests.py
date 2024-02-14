from django.test import TestCase

# Create your tests here.
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
        """
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

        # Additional model-specific tests could be added here

class DepartmentViewTest(TestCase):
    """
    Tests for the create_department view.
    """

    def test_get_create_department_view(self):
        """
        Tests that the create_department view renders the correct template.
        """
        response = self.client.get('/create_department/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_department.html')

    def test_post_create_department_view_valid_data(self):
        """
        Tests that the create_department view redirects to the success page on valid form submission.
        """
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
""""
    def test_post_create_department_view_invalid_data(self):
        
        Tests that the create_department view renders the template with errors on invalid form submission.
        
        data = {'name': ''}  # Missing required field
        response = self.client.post('/create_department/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_department.html')
        self.assertFormError(response, 'form', 'name', 'This field is required.')
"""
