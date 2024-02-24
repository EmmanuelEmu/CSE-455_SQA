from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Student(models.Model):
    """
    Model representing a student.

    Attributes:
        name (str): The name of the student.
        hsc_roll (str): The roll number of the student for HSC exam.
        hsc_reg (str): The registration number of the student for HSC exam.
        reg_no (str): The registration number of the student.
        roll (str): The roll number of the student.
        session (str): The session of the student.
        email (str): The email address of the student.
        phone (str): The phone number of the student.
        dob (str): The date of birth of the student.
        address (str): The address of the student.
        fathers_name (str): The name of the student's father.
        mothers_name (str): The name of the student's mother.
        guardian_phone (str): The phone number of the student's guardian.
        description (str): Additional description about the student.
        status (str): The status of the student, choices are 'Regular' or 'Ex-Student'.
        CGPA (float): The Cumulative Grade Point Average of the student.
        result_description (str): Description of the student's results.

    Methods:
        __str__(): Returns the name of the student as a string.
    """
    
    STATUS=(
            ('Regular','Regular'),
            ('Ex-Student','Ex-Student'),
        )

    
    name=models.CharField(max_length=30,null=False)
    hsc_roll=roll=models.CharField(max_length=10,null=True,unique=True)
    hsc_reg=models.CharField(max_length=16,null=True,unique=True)
    reg_no=models.CharField(max_length=16,null=True,unique=True,blank=True)
    roll=models.CharField(max_length=10,null=True,unique=True,blank=True)
    
    session=models.CharField(max_length=10,null=True)
    email=models.EmailField()
    phone=models.CharField(max_length=20,null=True)
    dob=models.CharField(max_length=30,null=True,blank=True)
    address=models.CharField(max_length=50,null=True)
    fathers_name=models.CharField(max_length=30,null=True)
    mothers_name=models.CharField(max_length=30,null=True)
    guardian_phone=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=3000,null=True,blank=True)
    
    status=models.CharField(max_length=40,null=True,default='Regular',choices=STATUS)
    CGPA = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0.0), MaxValueValidator(4.0)])
    result_description=models.CharField(default="No Details Available now.",max_length=3000,null=True,blank=True)

    def __str__(self):
       return self.name