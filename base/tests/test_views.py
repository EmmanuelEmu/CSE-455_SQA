from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpRequest
from base.models import Student
from base.forms import StudentForm
from django.core.exceptions import ObjectDoesNotExist
from base.views import create_student

class TestCommonPageView(TestCase):

    def setUp(self):
        self.client = Client()
        self.common_page_url = reverse('common_page')  # Replace 'common_page' with your actual URL name

    def test_common_page_view(self):
        # Simulate a GET request to the common_page view
        response = self.client.get(self.common_page_url)

        # Assert that the response status code is 200, indicating success
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is being used to render the response
        self.assertTemplateUsed(response, 'base/common_page.html')

        # You can add more specific assertions here if needed


   

    


class StudentViewsTest(TestCase):
      def setUp(self):
            self.client = Client()
            self.student = Student.objects.create(name='Test Student')

      def test_studentinfo_get_request(self):
        
        response = self.client.get(reverse('student_info', args=[self.student.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/student_info.html')
        self.assertEqual(response.context['student'], self.student)


class TestCreateStudentView(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_create_student_view_get(self):
        # Simulate a GET request to the create_student view
        response = self.client.get(reverse('create_student'))

        # Assert that the response status code is 200, indicating success
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is being used to render the response
        self.assertTemplateUsed(response, 'base/create_student.html')

        # You can add more specific assertions here if needed

    def test_create_student_view_post_valid_form(self):
        # Simulate a POST request to the create_student view with a valid form submission
        form_data = {
            'name': 'Ali ahmed',
            'hsc_roll': '12345',
            'hsc_reg': '43123',
            'reg_no': '4324456',
            'roll': '43789',
            'session': '2018-2019',
            'email': 'ali@gmail.com',
            'phone': '1234567890',
            'dob': '10-01-2000',
            'address': 'dhaka',
            'fathers_name': 'hasan ali',
            'mothers_name': 'afroza khatun',
            'guardian_phone': '9876543210',
            'description': 'first year',
            'status': 'Regular',
            'CGPA': 3.5,
            'result_description': 'Good performance',
            # Add other form fields as needed
        }
        response = self.client.post(reverse('create_student'), data=form_data)
        self.assertEqual(response.status_code, 302)

        # Assert that the student was created in the database
        self.assertTrue(Student.objects.filter(name='Ali ahmed').exists())
        self.assertTrue(Student.objects.filter(hsc_roll='12345').exists())
        self.assertTrue(Student.objects.filter(hsc_reg='43123').exists())
        self.assertTrue(Student.objects.filter(reg_no= '4324456').exists())
        self.assertTrue(Student.objects.filter(roll='43789').exists())
        self.assertTrue(Student.objects.filter(session='2018-2019').exists())
        self.assertTrue(Student.objects.filter(email='ali@gmail.com').exists())
        self.assertTrue(Student.objects.filter(phone= '1234567890').exists())
        self.assertTrue(Student.objects.filter(dob='10-01-2000').exists())
        self.assertTrue(Student.objects.filter(address='dhaka').exists())
        self.assertTrue(Student.objects.filter(fathers_name='hasan ali').exists())
        self.assertTrue(Student.objects.filter(mothers_name='afroza khatun').exists())
        self.assertTrue(Student.objects.filter(guardian_phone='9876543210').exists())
        self.assertTrue(Student.objects.filter(description='first year').exists())
        self.assertTrue(Student.objects.filter(status='Regular').exists())
        self.assertTrue(Student.objects.filter(CGPA=3.5).exists())
        self.assertTrue(Student.objects.filter(result_description='Good performance').exists())

        # You can add more specific assertions here if needed



class TestUpdateStudentView(TestCase):
    
    def setUp(self):
        self.client = Client()
        # Create a user for authentication purposes if needed
        #self.user = User.objects.create_user(username='testuser', password='password123')

    def test_update_student_view_get(self):
        # Create a student instance for testing
        student = Student.objects.create(name='Test Student', hsc_roll='12345')
        
        # Simulate a GET request to the update_student view
        response = self.client.get(reverse('update_student', args=[student.pk]))

        # Assert that the response status code is 200, indicating success
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is being used to render the response
        self.assertTemplateUsed(response, 'base/create_student.html')

        # You can add more specific assertions here if needed

    def test_update_student_view_post_valid_form(self):
        # Create a student instance for testing
        student = Student.objects.create(name='Test Student', hsc_roll='12345')

        # Simulate a POST request to the update_student view with a valid form submission
        form_data = {
            'name': 'Ali Ahmed',
            'hsc_roll': '12345',  # hsc_roll remains the same
            'hsc_reg': '43123',
            'reg_no': '4324456',
            'roll': '43789',
            'session': '2018-2019',
            'email': 'ali@gmail.com',
            'phone': '1234567890',
            'dob': '2000-01-10',  # Use ISO format for dates
            'address': 'Dhaka',
            'fathers_name': 'Hasan Ali',
            'mothers_name': 'Afroza Khatun',
            'guardian_phone': '9876543210',
            'description': 'First year',
            'status': 'Regular',
            'CGPA': 3.5,
            'result_description': 'Good performance',
            # Add other form fields as needed
        }
        response = self.client.post(reverse('update_student', args=[student.pk]), data=form_data)
        
        # Assert that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Assert that the student instance was updated in the database
        updated_student = Student.objects.get(pk=student.pk)
        self.assertEqual(updated_student.name, 'Ali Ahmed')
        self.assertEqual(updated_student.hsc_reg, '43123')
        self.assertEqual(updated_student.reg_no, '4324456')
        self.assertEqual(updated_student.roll, '43789')
        self.assertEqual(updated_student.session, '2018-2019')
        self.assertEqual(updated_student.email, 'ali@gmail.com')
        self.assertEqual(updated_student.phone, '1234567890')
        self.assertTrue(updated_student.dob,'10-01-2000')
        self.assertEqual(updated_student.address, 'Dhaka')
        self.assertEqual(updated_student.fathers_name, 'Hasan Ali')
        self.assertEqual(updated_student.mothers_name, 'Afroza Khatun')
        self.assertEqual(updated_student.guardian_phone, '9876543210')
        self.assertEqual(updated_student.description, 'First year')
        self.assertEqual(updated_student.status, 'Regular')
        self.assertEqual(updated_student.CGPA, 3.5)
        self.assertEqual(updated_student.result_description, 'Good performance')