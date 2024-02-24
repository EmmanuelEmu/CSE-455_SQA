from django.test import TestCase
from base.models import Student
from base.filters import StudentFilter



class StudentFilterTest(TestCase):
    """
    Test case for the StudentFilter class.

    Inherits from:
    - TestCase: Django's built-in test case class.

    Attributes:
    - student1: Sample instance of the Student model for testing.
    - student2: Sample instance of the Student model for testing.
    - student3: Sample instance of the Student model for testing.

    Methods:
    - setUp: Method to set up sample data for testing.
    - test_student_filter: Method to test the functionality of the StudentFilter.

    Usage:
    This test case is designed to test the filtering functionality of the StudentFilter class.


    Sphinx Tags:

    - :meth setUp: Method to set up sample data for testing.
    - :meth test_student_filter: Method to test the functionality of the StudentFilter.

    Django Models:
    - Student: The Django model representing student information.
    - StudentFilter: The filter class for the Student model.

    Dependencies:
    - Django must be properly installed in the project.
    - TestCase class should be imported from 'django.test'.
    - Student model and StudentFilter class should be imported from the appropriate module.

    Notes:
    The test case sets up sample data with three student instances and tests the filtering
    functionality of the StudentFilter class using a predefined set of filter data.

    """
    def setUp(self):
        """
        Set up sample data for testing.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.
        - :student2: Sample instance of the Student model for testing.
        - :student3: Sample instance of the Student model for testing.

        """
        # Create some sample data for testing
        self.student1 = Student.objects.create(id=1, name="John Doe", roll="001", CGPA_gt=3.7, status='Regular')
        self.student2 = Student.objects.create(id=2, name="Jane Doe", roll="002", CGPA_gt=4.0, status='Ex-Student')
        self.student3 = Student.objects.create(id=3, name="Bob Smith", roll="003", CGPA_gt=3.8, status='Regular')

    def test_student_filter(self):
        """
        Test the functionality of the StudentFilter.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Define the filter data
        filter_data = {
            'id': 1,
            'roll': "001",
            'name': "John Doe",
        }

        # Create a filter instance with the provided data
        student_filter = StudentFilter(data=filter_data)

        # Validate that the filter is valid
        self.assertTrue(student_filter.is_valid())

        # Apply the filter to the queryset
        filtered_students = student_filter.qs

        # Assert the expected result based on the filter data
        self.assertEqual(filtered_students.count(), 1)
        self.assertEqual(filtered_students[0], self.student1)