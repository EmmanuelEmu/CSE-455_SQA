from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
        
