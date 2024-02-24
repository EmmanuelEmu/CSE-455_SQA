from django.forms import ModelForm
from .models import *
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User





class CreateUserForm(UserCreationForm):
    """
    Custom form class for user registration with additional fields.

    Usage:
    This form is intended to be used for user registration, extending Django's UserCreationForm
    with additional fields such as email.


    Notes:
    The form includes fields such as username, email, password1, and password2.
    It is designed to work seamlessly with Django's user registration and authentication system.

    """
    class Meta:
        """
        Metadata class for CreateUserForm.

        The fields to include in the form.

        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']





class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields='__all__'



