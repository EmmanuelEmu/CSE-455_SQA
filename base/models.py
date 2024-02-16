from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



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
