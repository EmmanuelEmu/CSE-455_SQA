from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse
from base.forms import TeacherForm  # Import your TeacherForm
from base.models import Teacher  # Import your Teacher model
from django.contrib.auth.models import User
from base.models import Student
from django.http import HttpRequest
from base.forms import StudentForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirectBase
from django.http import HttpResponseRedirect
from base.views import create_student
from base.forms import AdminNoticeForm  # Make sure to import your form
from base.models import AdminNotice

class CreateTeacherViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_teacher_url = reverse('create_teacher')  # Assuming 'create_teacher' is the name of your URL pattern
        self.home_url = reverse('home')
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_teacher_post(self):
        # Assuming valid form data
        form_data = {
            'name': 'Test Teacher',
            'reg_no': '123456',
            'rank': 'Lecturer',
            'dept': '',  # Pass an empty string for the dept field
            'email': 'test@example.com',
            'phone': '1234567890',
            'description': 'Test description'
        }

        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.create_teacher_url, form_data)

        # Check if the teacher was created successfully and redirected to 'home'
        self.assertEqual(response.status_code, 302)  # 302 is the status code for redirect
        self.assertEqual(response.url, reverse('home'))  # Assuming 'home' is the name of your home URL pattern
        # self.assertRedirects(response, self.home_url)
        self.assertTrue(Teacher.objects.filter(name='Test Teacher').exists())
    


    def test_create_teacher_invalid_form(self):
        # Assuming invalid form data
        invalid_form_data = {
            'name': 'Test Teacher',
            'reg_no': '123456',
            'rank': 'Lecturer',
            'dept': '',  # Pass an empty string for the dept field
            'email': 'test@example.com',
            'phone': '1234567890',
            'description': 'Test description'
        }

        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.create_teacher_url, invalid_form_data)

        # Check if the form is re-rendered with errors
        self.assertEqual(response.status_code, 200)  # 200 is the status code for successful HTTP response
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'subject', 'This field is required.')
        # Add more assertions for other fields as necessary

    def test_create_teacher_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.create_teacher_url)

        # Check if the response is successful and the correct template is rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_teacher.html')
from base.models import Teacher

class TeacherInfoViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.teacher = Teacher.objects.create(name='Test Teacher')

    def test_teacher_info_view(self):
        response = self.client.get(reverse('teacher_info', args=[self.teacher.pk]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/teacher_info.html')
        self.assertEqual(response.context['teacher'], self.teacher)


class TestCommonPageView(TestCase):

    def setUp(self):
        self.client = Client()
        self.common_page_url = reverse('common_page') 

    def test_common_page_view(self):
  
        response = self.client.get(self.common_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/common_page.html')


class TestCreateStudentView(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_create_student_view_get(self):
        
        response = self.client.get(reverse('create_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_student.html')

        

    def test_create_student_view_post_valid_form(self):
        
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
           
        }
        response = self.client.post(reverse('create_student'), data=form_data)
        self.assertEqual(response.status_code, 302)
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


def test_create_student_view_post_invalid_form(self):
       
        form_data = {
            # 'name': 'Ali ahmed',
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
        }
        response = self.client.post(reverse('create_student'), data=form_data)
        self.assertEqual(response.status_code, 200)  
        self.assertFormError(response, 'form', 'name', 'This field is required.')  

class StudentViewsTest(TestCase):
      def setUp(self):
            self.client = Client()
            self.student = Student.objects.create(name='Test Student')

      def test_studentinfo_get_request(self):
        
        response = self.client.get(reverse('student_info', args=[self.student.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/student_info.html')
        self.assertEqual(response.context['student'], self.student)


class CreateNoticeViewTest(TestCase):
    """
    Test case for the 'create_notice' view in the 'base' app.

    This test case checks the behavior of the 'create_notice' view with valid and invalid form data.
    """
    def setUp(self):
        """
        Set up necessary data for the test case.
        """
        self.client = Client()

    def test_create_notice_view(self):
        """
        Test the 'create_notice' view with valid form data.

        This test makes a POST request with valid form data, checks if the response redirects to the 'home' page,
        and verifies that a notice was created in the database.
        """
        # Define the URL for the create_notice view
        url = reverse('create_notice')

        # Make a POST request with valid form data
        data = {
            'sender': 'Admin',
            'receiver': 'JohnDoe',
            'subject': 'Test Subject',
            'body': 'Test Body',
        }
        response = self.client.post(url, data)

        # Check if the response redirects to the 'home' page
        self.assertRedirects(response, reverse('home'))

        # Check if a notice was created in the database
        self.assertEqual(AdminNotice.objects.count(), 1)

        # Optionally, you can check other details about the created notice

    def test_create_notice_view_invalid_form(self):
        """
        Test the 'create_notice' view with invalid form data.

        This test makes a POST request with invalid form data, checks if the response renders the 'create_notice' template,
        and ensures that the form in the context is an instance of AdminNoticeForm.
        """
        # Define the URL for the create_notice view
        url = reverse('create_notice')

        # Make a POST request with invalid form data
        data = {
            # Missing required fields
        }
        response = self.client.post(url, data)

        # Check if the response renders the create_notice template
        self.assertTemplateUsed(response, 'base/create_notice.html')

        # Check if the form in the context is an instance of AdminNoticeForm
        self.assertIsInstance(response.context['form'], AdminNoticeForm)

        # Check if the notice count in the database remains unchanged
        self.assertEqual(AdminNotice.objects.count(), 0)

        # Optionally, you can check other details about the response



class NoticeDetailsViewTest(TestCase):
    """
    Test case for the 'notice_details' view in the 'base' app.

    This test case checks the behavior of the 'notice_details' view with valid and invalid notice IDs.
    """
    def setUp(self):
        """
        Set up necessary data for the test case.
        """
        # Create a sample notice for testing
        self.notice = AdminNotice.objects.create(
            sender="Admin",
            receiver="JohnDoe",
            subject="Test Subject",
            body="Test Body",
        )
        self.client = Client()

    def test_notice_details_view(self):
        """
        Test the 'notice_details' view with a valid notice ID.

        This test makes a GET request to the 'notice_details' view, checks if the response is as expected,
        and verifies that the notice in the context matches the created notice.
        """
        # Define the URL for the notice_details view with the notice's ID
        url = reverse('notice_details', args=[self.notice.id])

        # Make a GET request to the notice_details view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered template is 'base/notice_details.html'
        self.assertTemplateUsed(response, 'base/notice_details.html')

        # Check if the notice in the context matches the created notice
        self.assertEqual(response.context['notice'], self.notice)

    def test_notice_details_view_invalid_id(self):
        """
        Test the 'notice_details' view with an invalid notice ID.

        This test makes a GET request to the 'notice_details' view with an invalid ID and expects an exception.
        """
    # Define an invalid notice ID
        invalid_id = 999

    # Define the URL for the notice_details view with the invalid ID
        url = reverse('notice_details', args=[invalid_id])

    # Make a GET request to the notice_details view with an invalid ID
        with self.assertRaises(AdminNotice.DoesNotExist):
            self.client.get(url)

    # No need to access the response variable here, as it's not expected to be defined

