from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.




class Department(models.Model):

    LOCATION=(
        ('Block A','Block A'),
        ('Block B','Block B'),
        ('Block C','Block C'),
        ('Block D','Block D'),
        ('Block E','Block E'),
    )
    

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

    STATUS=(
            ('Regular','Regular'),
            ('Ex-Student','Ex-Student'),
        )

    
    name=models.CharField(max_length=30,null=False)
    hsc_roll=roll=models.CharField(max_length=10,null=True,unique=True)
    hsc_reg=models.CharField(max_length=16,null=True,unique=True)
    reg_no=models.CharField(max_length=16,null=True,unique=True,blank=True)
    roll=models.CharField(max_length=10,null=True,unique=True,blank=True)
    dept=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL,blank=True)
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

    


class Teacher(models.Model):  
    RANK=(
        ('Lecturer','Lecturer'),
        ('Assistant Professor','Assistant Professor'),
        ('Professor','Professor'),
        ('Head of The Department','Head of The Department'),
    )

    name=models.CharField(max_length=30,null=False)
    reg_no=models.CharField(max_length=10,null=False,unique=True)
    rank=models.CharField(max_length=40,null=True,choices=RANK)
    dept=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    email=models.EmailField()
    phone=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=3000,null=True)

    def __str__(self):
       return self.name
    



class AdminNotice(models.Model):


    sender=models.CharField(max_length=30,null=False,default="Admin")
    receiver=models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.subject

