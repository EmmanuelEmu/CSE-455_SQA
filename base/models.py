from django.db import models




class Department(models.Model):

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
    """
    Description about the teacher.

    :type: str
    """

    def __str__(self):
       return self.name
    