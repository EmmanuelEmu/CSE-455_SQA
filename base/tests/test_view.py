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



    