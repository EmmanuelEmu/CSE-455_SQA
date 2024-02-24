from django.test import TestCase
from base.forms import DepartmentForm
from base.models import Department

"""
.. module:: base.tests
   :synopsis: Tests for the base app.

TestDepartmentForm
------------------

.. autoclass:: base.tests.TestDepartmentForm
   :members:
   :undoc-members:
   :show-inheritance:


   Unit tests for the DepartmentForm class.

   This class contains test cases for validating the functionality of the DepartmentForm.

   .. automethod:: test_valid_form
   .. automethod:: test_invalid_form
   .. automethod:: test_save_form
   .. automethod:: test_update_form
"""

class TestDepartmentForm(TestCase):
    """
    Unit tests for the DepartmentForm class.

    This class contains test cases for validating the functionality of the DepartmentForm.
    """

    def test_valid_form(self):
        """
        Test if the form is valid when all required fields are provided.
        """
        form_data = {
            'name': 'Test Department',
            'location': 'Block A',
            'rank': 1,
            'phone': '1234567890',
            'email': 'test@example.com',
            'description': 'Test Description'
        }
        form = DepartmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Test if form is invalid when required fields are missing.
        """
        form = DepartmentForm(data={})
        self.assertFalse(form.is_valid())

    def test_save_form(self):
        """
        Test if form saves the data correctly.
        """
        form_data = {
            'name': 'Test Department',
            'location': 'Block A',
            'rank': 1,
            'phone': '1234567890',
            'email': 'test@example.com',
            'description': 'Test Description'
        }
        form = DepartmentForm(data=form_data)
        self.assertTrue(form.is_valid())
        department = form.save()
        self.assertEqual(department.name, 'Test Department')
        self.assertEqual(department.location, 'Block A')
        self.assertEqual(department.rank, 1)
        self.assertEqual(department.phone, '1234567890')
        self.assertEqual(department.email, 'test@example.com')
        self.assertEqual(department.description, 'Test Description')

    def test_update_form(self):
        """
        Test if form updates the data correctly.
        """
        department = Department.objects.create(
            name='Original Name',
            location='Block B',
            rank=2,
            phone='9876543210',
            email='original@example.com',
            description='Original Description'
        )
        form_data = {
            'name': 'Updated Name',
            'location': 'Block C',
            'rank': 3,
            'phone': '9999999999',
            'email': 'updated@example.com',
            'description': 'Updated Description'
        }
        form = DepartmentForm(data=form_data, instance=department)
        self.assertTrue(form.is_valid())
        updated_department = form.save()
        self.assertEqual(updated_department.name, 'Updated Name')
        self.assertEqual(updated_department.location, 'Block C')
        self.assertEqual(updated_department.rank, 3)
        self.assertEqual(updated_department.phone, '9999999999')
        self.assertEqual(updated_department.email, 'updated@example.com')
        self.assertEqual(updated_department.description, 'Updated Description')
