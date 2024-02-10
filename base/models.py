from django.db import models

# Create your models here.
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
    