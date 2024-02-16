from django.forms import ModelForm
from .models import *
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User





class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        
class TeacherForm(forms.ModelForm):
    """
    Form for creating or updating a teacher.

    This form is used to create or update instances of the Teacher model.
    It inherits from Django's ModelForm class and automatically generates
    form fields based on the Teacher model's fields.

    Example usage:

    .. code-block:: python

        # Create a form instance
        form = TeacherForm()

        # Process form submission
        if request.method == 'POST':
            form = TeacherForm(request.POST)
            if form.is_valid():
                # Save the form data to create or update a Teacher instance
                form.save()

    For more information on working with Django forms, see:
    https://docs.djangoproject.com/en/stable/topics/forms/

    """    
    class Meta:
        
        model = Teacher
        fields = '__all__'