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