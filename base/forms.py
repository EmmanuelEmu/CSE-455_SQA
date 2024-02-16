from django.forms import ModelForm
from .models import *
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


        
class StudentForm(ModelForm):
    """
    Form for creating and updating Student objects.

    Inherits from:
        ModelForm: A form that automatically generates form fields based on the Student model.

    Attributes:
        Meta: A inner class that defines metadata options for the form.
            model (Model): The model associated with the form (Student).
            fields (list or tuple): The fields to include in the form. Here, '__all__' includes all fields.

    Example:
        To use this form in a view, simply instantiate it:

        >>> form = StudentForm()
    """
    class Meta:
        model = Student
        fields='__all__'