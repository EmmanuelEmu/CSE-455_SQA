from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.




class Department(models.Model):


    """
    Model representing a department.

    Attributes:
    - name (CharField): The name of the department.
    - location (CharField): The location of the department (chosen from predefined options).
    - rank (IntegerField): The rank of the department.
    - phone (CharField): The phone number of the department.
    - email (CharField): The email address of the department.
    - date_created (DateTimeField): The date and time when the department was created.
    - description (CharField): A description of the department.

    Methods:
    - __str__(): Returns the string representation of the department (its name).
    """

    LOCATION=(
        ('Block A','Block A'),
        ('Block B','Block B'),
        ('Block C','Block C'),
        ('Block D','Block D'),
        ('Block E','Block E'),
    )
    

    #user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True,)
    location = models.CharField(max_length=20, null=True, choices=LOCATION)
    rank=models.IntegerField(null=True,blank=True)
    phone=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=30,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=3000,null=True,blank=True)
    def __str__(self):
       return self.name




class Student(models.Model):


    """
    Model representing a student.

    Attributes:
    - name (CharField): The name of the student.
    - hsc_roll (CharField): The Higher Secondary Certificate (HSC) roll number of the student.
    - hsc_reg (CharField): The HSC registration number of the student.
    - reg_no (CharField): The registration number of the student.
    - roll (CharField): The roll number of the student.
    - session (CharField): The session in which the student is enrolled.
    - email (EmailField): The email address of the student.
    - phone (CharField): The phone number of the student.
    - dob (CharField): The date of birth of the student.
    - address (CharField): The address of the student.
    - fathers_name (CharField): The name of the student's father.
    - mothers_name (CharField): The name of the student's mother.
    - guardian_phone (CharField): The phone number of the student's guardian.
    - description (CharField): A description of the student.
    - status (CharField): The status of the student (chosen from predefined options).
    - CGPA (FloatField): The Cumulative Grade Point Average of the student.
    - result_description (CharField): A description of the student's academic result.

    Methods:
    - __str__(): Returns the string representation of the student (its name).
    """


    STATUS=(
            ('Regular','Regular'),
            ('Ex-Student','Ex-Student'),
        )

    #user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=False)
    hsc_roll=roll=models.CharField(max_length=10,null=True,unique=True)
    hsc_reg=models.CharField(max_length=16,null=True,unique=True)
    reg_no=models.CharField(max_length=16,null=True,unique=True,blank=True)
    roll=models.CharField(max_length=10,null=True,unique=True,blank=True)
    #dept=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL,blank=True)
    session=models.CharField(max_length=10,null=True)
    email=models.EmailField()
    phone=models.CharField(max_length=20,null=True)
    dob=models.CharField(max_length=30,null=True,blank=True)
    address=models.CharField(max_length=50,null=True)
    fathers_name=models.CharField(max_length=30,null=True)
    mothers_name=models.CharField(max_length=30,null=True)
    guardian_phone=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=3000,null=True,blank=True)
    #profile_pic=models.ImageField(default="profile1.png",null=True,blank=True)
    status=models.CharField(max_length=40,null=True,default='Regular',choices=STATUS)
    CGPA = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0.0), MaxValueValidator(4.0)])
    result_description=models.CharField(default="No Details Available now.",max_length=3000,null=True,blank=True)

    def __str__(self):
       return self.name