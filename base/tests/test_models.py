from django.test import TestCase
from base.models import Student

class StudentModelTest(TestCase):
    """
        Test case to create a student instance and verify its attributes.
    """
    def test_create_student(self):
        student = Student.objects.create(
            name="Rafi Kibria",
            hsc_roll="12345",
            hsc_reg="ABCD1234",
            reg_no="XYZ12345",
            roll="12301",
            session="2018-2019",
            email="stu@gmail.com",
            phone="0158655554",
            dob='2000-01-01',
            address='123 Main St',
            fathers_name='John Doe Sr.',
            mothers_name='Jane Doe',
            guardian_phone='0987654321',
            description='keep doing hard work ',
            status='Regular',
            CGPA=3.5,
            result_description='Try best until your dreams come true. Best of luck.'
        )

        self.assertEqual(student.name, "Rafi Kibria")
        self.assertEqual(student.hsc_roll, "12345")
        self.assertEqual(student.hsc_reg, "ABCD1234")
        self.assertEqual(student.reg_no, "XYZ12345")
        self.assertEqual(student.roll, "12301")
        self.assertEqual(student.session, "2018-2019")
        self.assertEqual(student.email, "stu@gmail.com")
        self.assertEqual(student.phone, "0158655554")
        self.assertEqual(student.dob, '2000-01-01')        
        self.assertEqual(student.address, '123 Main St')        
        self.assertEqual(student.fathers_name, 'John Doe Sr.')        
        self.assertEqual(student.mothers_name, 'Jane Doe')        
        self.assertEqual(student.guardian_phone, '0987654321')        
        self.assertEqual(student.description, 'keep doing hard work ')        
        self.assertEqual(student.status, 'Regular')        
        self.assertEqual(student.CGPA, 3.5)        
        self.assertEqual(student.result_description, 'Try best until your dreams come true. Best of luck.')
