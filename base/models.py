from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


'''
Department Model
================

.. currentmodule:: myapp.models

.. autoclass:: Department
   :members:
   :undoc-members:
   :show-inheritance:

'''


class Department(models.Model):
    """
    Model representing a department in your organization.

    Attributes:
        name (str): The name of the department.
        location (str): The location of the department. Choices are 'Block A', 'Block B', 'Block C', 'Block D', 'Block E'.
        rank (int): The rank of the department.
        phone (str): The phone number of the department.
        email (str): The email address of the department.
        date_created (datetime): The date and time when the department was created.
        description (str): A description of the department.
    """

    LOCATION = (
        ('Block A', 'Block A'),
        ('Block B', 'Block B'),
        ('Block C', 'Block C'),
        ('Block D', 'Block D'),
        ('Block E', 'Block E'),
    )

    name = models.CharField(max_length=30, null=True, help_text="Enter the department's name.")
    location = models.CharField(max_length=20, null=True, choices=LOCATION, help_text="Select the department's location.")
    rank = models.IntegerField(null=True, blank=True, help_text="Enter the department's rank.")
    phone = models.CharField(max_length=20, null=True, help_text="Enter the department's phone number.")
    email = models.CharField(max_length=30, null=True, help_text="Enter the department's email address.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time when the department was created.")
    description = models.CharField(max_length=3000, null=True, blank=True, help_text="Enter a description of the department.")

    def __str__(self):
        return self.name


# Create your models here.

class Teacher(models.Model):  
    """
    Model representing a teacher.
    """
    RANK=(
        ('Lecturer','Lecturer'),
        ('Assistant Professor','Assistant Professor'),
        ('Professor','Professor'),
        ('Head of The Department','Head of The Department'),
    )

    name=models.CharField(max_length=30,null=False)
    """
    The name of the teacher.

    :type: str
    """
    reg_no=models.CharField(max_length=10,null=False,unique=True)
    """
    The registration number of the teacher.

    :type: str
    """
    rank=models.CharField(max_length=40,null=True,choices=RANK)
    """
    The rank of the teacher.

    :type: str
    :choices: 'Lecturer', 'Assistant Professor', 'Professor', 'Head of The Department'
    """
    dept=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    """
    The department to which the teacher belongs.

    :type: Department
    """
    email=models.EmailField()
    """
    The email address of the teacher.

    :type: str
    """
    phone=models.CharField(max_length=20,null=True)
    """
    The phone number of the teacher.

    :type: str
    """
    description=models.CharField(max_length=3000,null=True)
    

    def __str__(self):
       return self.name
    
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

# Create your models here.


class AdminNotice(models.Model):
    """
    Model representing an administrative notice.

    Attributes:
        sender (str): The sender of the notice.
        receiver (str): The intended receiver of the notice.
        subject (str): The subject of the notice.
        body (str): The content or body of the notice.
        date_sent (datetime): The date and time when the notice was sent.

    Methods:
        __str__: Returns a string representation of the notice, which is its subject.
    """


    sender=models.CharField(max_length=30,null=False,default="Admin")
    receiver=models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)


   
       
    def __str__(self):
        """
        Returns a string representation of the notice.

        Returns:
            str: The subject of the notice.
   """
        return self.subject
        
