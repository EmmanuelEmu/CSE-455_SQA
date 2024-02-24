from django.test import TestCase, Client, RequestFactory
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
from base.views import update_teacher

from base.views import department_info
from base.models import Department
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from base.views import update_department
from base.forms import DepartmentForm
from django.urls import reverse




from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from base.forms import CreateUserForm
from django.http import HttpRequest
from base.models import Student
from base.forms import StudentForm
from django.core.exceptions import ObjectDoesNotExist
from base.views import create_student




class NavStuListTest(TestCase):
    """
    Test case for the nav_stu_list.

    Inherits from:
    - TestCase: Django's built-in test case class.

    Attributes:
    - student1: Sample instance of the Student model for testing.
    - student2: Sample instance of the Student model for testing.
    - student3: Sample instance of the Student model for testing.

    Methods:
    - setUp: Method to set up sample data for testing.
    - test_nav_stu_list_view: Method to test the functionality of the nav_stu_list view.

    Usage:
    This test case is designed to test the functionality of the nav_stu_list view including basic rendering
    and filtering.


    Django Models:
    - Student: The Django model representing student information.

    Dependencies:
    - Django must be properly installed in the project.
    - TestCase class should be imported from 'django.test'.
    - Client class and reverse function should be imported from 'django.test.client'.
    - Student model should be imported from the appropriate module.


    Notes:
    The test case sets up sample data with three student instances and tests the rendering and filtering
    functionality of the NavStuList view using Django's test client.

    """
    def setUp(self):
        """
        Set up sample data for testing.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Create some sample data for testing
        self.student1 = Student.objects.create(
            name="John", roll="001", CGPA=3.7, status='Regular'
        )
        self.student2 = Student.objects.create(
            name="Jane", roll="002", CGPA=3.0, status='Ex-Student'
        )
        self.student3 = Student.objects.create(
            name="Smith", roll="003", CGPA=3.8, status='Regular'
        )

    def test_nav_stu_list_view(self):
        """
        Test the functionality of the nav_stu_list view.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Create a client for making requests
        client = Client()

        # Make a GET request to the view
        response = client.get(reverse('nav_stu_list'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered HTML contains the names of the students
        self.assertContains(response, 'John')
        self.assertContains(response, 'Jane')
        self.assertContains(response, 'Smith')

        # Test the filtering by providing query parameters in the request
        response_filtered = client.get(reverse('nav_stu_list'), {'status': 'Regular'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response_filtered.status_code, 200)

        # Check if the rendered HTML contains the filtered students
        self.assertContains(response_filtered, 'John')
        self.assertNotContains(response_filtered, 'Jane')
        self.assertContains(response_filtered, 'Smith')







class DeleteStudentTest(TestCase):
    """
    Test case for the delete_student.

    Inherits:
    - TestCase: Django's built-in test case class.

    Attributes:
    - student1: Sample instance of the Student model for testing.

    Methods:
    - setUp: Method to set up sample data for testing.
    - test_delete_student_view: Method to test the functionality of the DeleteStudent view.

    Usage:
    This test case is designed to test the functionality of the DeleteStudent view, including rendering
    and the deletion of a student.

   
    Django Models:
    - Student: The Django model representing student information.

    Dependencies:
    - Django must be properly installed in the project.
    - TestCase class should be imported from 'django.test'.
    - Client class and reverse function should be imported from 'django.test.client'.



    Notes:
    The test case sets up sample data with one student instance and tests the rendering and deletion
    functionality of the delete_student view using Django's test client.

    """
    def setUp(self):
        """
        Set up sample data for testing.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Create some sample data for testing
        self.student1 = Student.objects.create(
            name="John", roll="001", status='Regular'
        )

    def test_delete_student_view(self):
        """
        Test the functionality of the delete_student view.

        Sphinx Tags:
        - :student1: Sample instance of the Student model for testing.

        """
        # Create a client for making requests
        client = Client()

        # Get the URL for deleting the student
        url = reverse('delete_student', args=[self.student1.id])

        # Make a GET request to the view
        response = client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered HTML contains the student's information
        self.assertContains(response, 'John')

        # Make a POST request to delete the student
        response_post = client.post(url)

        # Check if the response redirects to 'home'
        self.assertRedirects(response_post, reverse('home'))

        # Check if the student is deleted
        self.assertEqual(Student.objects.count(), 0)









class TestCommonPageView(TestCase):
    """
    Test case for the common_page view.

    Methods:
    - setUp(): Set up necessary variables for testing.
    - test_common_page_view(): Test the common_page view.
    """

    def setUp(self):
        """
        Set up necessary variables for testing.

        Creates a test client and defines the common_page URL.
        """
        self.client = Client()
        self.common_page_url = reverse('common_page') 

    def test_common_page_view(self):
        """
        Test the common_page view.

        Simulates a GET request to the common_page view and asserts the response status code and template used.
        """
        response = self.client.get(self.common_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/common_page.html')


class TestRegister(TestCase):
    """
    Test case for the register view.

    Methods:
    - setUp(): Set up necessary variables for testing.
    - test_register_view_get(): Test the GET request to the register view.
    - test_register_view_post_valid_form(): Test the POST request to the register view with a valid form.
    """

    def setUp(self):
        """
        Set up necessary variables for testing.

        Creates a test client and defines the register and login URLs.
        """
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_register_view_get(self):
        """
        Test the GET request to the register view.

        Simulates a GET request to the register view and asserts the response status code and template used.
        """
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register.html')

    def test_register_view_post_valid_form(self):
        """
        Test the POST request to the register view with a valid form.

        Simulates a POST request to the register view with valid form data and asserts the redirection to the login page.
        """
        form_data = {
            'username': 'testuser',
            'email':'email@gmail.com',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!'
        }
        response = self.client.post(self.register_url, data=form_data)
        self.assertRedirects(response, self.login_url)


class TestLoginAdmin(TestCase):
    """
    Test case for the login_admin view.

    Methods:
    - setUp(): Set up necessary variables for testing.
    - test_login_admin_view_incorrect_credentials(): Test the login_admin view with incorrect credentials.
    - test_login_admin_view_correct_credentials(): Test the login_admin view with correct credentials.
    """

    def setUp(self):
        """
        Set up necessary variables for testing.

        Creates a test user for login attempts.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_admin_view_incorrect_credentials(self):
        """
        Test the login_admin view with incorrect credentials.

        Simulates a login attempt with incorrect credentials and asserts the response status code and error message.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('login'), {
            'username': 'incorrect_user',
            'password': 'incorrect_password'
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username or Password is incorrect")

    def test_login_admin_view_correct_credentials(self):
        """
        Test the login_admin view with correct credentials.

        Simulates a login attempt with correct credentials and asserts the successful redirection to the home page.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('home')))


class TestLogoutAdmin(TestCase):
    """
    Test case for the logout_user view.

    Methods:
    - test_logout_user_view(): Test the logout_user view.
    """

    def test_logout_user_view(self):
        """
        Test the logout_user view.

        Simulates a GET request to the logout_user view and asserts the response status code.
        """
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)






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

class TeacherUpdateTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.teacher = Teacher.objects.create(name='John Doe', email='john@example.com')  # Create a sample teacher

    def test_update_teacher(self):
        url = reverse('update_teacher', args=(self.teacher.pk,))
        data = {'name': 'Jane Doe', 'email': 'jane@example.com'}
        request = self.factory.post(url, data)
        response = update_teacher(request, pk=self.teacher.pk)
        self.assertEqual(response.status_code, 302)  # Check if redirected after successful form submission
        updated_teacher = Teacher.objects.get(pk=self.teacher.pk)
        self.assertEqual(updated_teacher.name, 'Jane Doe')  # Check if name is updated correctly
        self.assertEqual(updated_teacher.email, 'jane@example.com')  # Check if email is updated correctly

        # Additional tests if needed

    def test_update_teacher_invalid_form(self):
        url = reverse('update_teacher', args=(self.teacher.pk,))
        data = {'name': '', 'email': 'jane@example.com'}  # Invalid form data
        request = self.factory.post(url, data)
        response = update_teacher(request, pk=self.teacher.pk)
        self.assertEqual(response.status_code, 200)  # Check if form is re-rendered
        # self.assertContains(response, 'This field is required.')  # Check if form errors are displayed

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
        """
        Setup method to initialize the test client.
        """
        self.client = Client()

    def test_create_student_view_get(self):
        """
        Test case to verify that the create student view returns a status code of 200 and uses the correct template for GET request.
        """
        response = self.client.get(reverse('create_student'))    
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_student.html')



    def test_create_student_view_post_valid_form(self):
        """
        Test case to verify that the create student view successfully creates a student object with valid form data.
        """
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




class TestUpdateStudentView(TestCase):
    """
    Test case for the update_student view.

    Methods:
        setUp(self): Prepares the test environment before each test method is run.
        test_update_student_view_get(self): Tests the GET request to the update_student view.
        test_update_student_view_post_valid_form(self): Tests the POST request with valid form data.

    """
    
    def setUp(self):
        """
        Set up the test environment.
        
        This method is called before each test method to set up any necessary preconditions.
        It initializes the test client.
        
        """
        self.client = Client()
        

    def test_update_student_view_get(self):
        """
        Test the GET request to the update_student view.

        Checks if the view returns a status code of 200 and uses the correct template.

        """
        student = Student.objects.create(name='Test Student', hsc_roll='12345')
        
        
        response = self.client.get(reverse('update_student', args=[student.pk]))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_student.html')

        

    def test_update_student_view_post_valid_form(self):
        """
        Test the POST request with valid form data.

        Checks if the view updates the student record correctly and redirects after a successful update.

        """
        
        student = Student.objects.create(name='Test Student', hsc_roll='12345')

        
        form_data = {
            'name': 'Ali Ahmed',
            'hsc_roll': '12345',  
            'hsc_reg': '43123',
            'reg_no': '4324456',
            'roll': '43789',
            'session': '2018-2019',
            'email': 'ali@gmail.com',
            'phone': '1234567890',
            'dob': '2000-01-10',  
            'address': 'Dhaka',
            'fathers_name': 'Hasan Ali',
            'mothers_name': 'Afroza Khatun',
            'guardian_phone': '9876543210',
            'description': 'First year',
            'status': 'Regular',
            'CGPA': 3.5,
            'result_description': 'Good performance',
            
        }
        response = self.client.post(reverse('update_student', args=[student.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)

    
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
class AdminNoticeViewTests(TestCase):
    def setUp(self):
        # Create a test user (optional)
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test notice
        self.notice = AdminNotice.objects.create(sender='Admin', receiver='Sizan')

    def test_update_notice_view_get(self):
        """
        Test that the update_notice view returns a form for updating an existing notice (GET request).
        """
        self.client.login(username='testuser', password='testpassword')  # If authentication is required
        url = reverse('update_notice', args=[self.notice.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/create_notice.html')
        self.assertIsInstance(response.context['form'], AdminNoticeForm)
        self.assertEqual(response.context['form'].instance, self.notice)


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

