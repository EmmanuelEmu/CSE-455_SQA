from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class AdminNotice(models.Model):


    sender=models.CharField(max_length=30,null=False,default="Admin")
    receiver=models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.subject
