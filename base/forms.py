from django.forms import ModelForm
from .models import *
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User





class CreateUserForm(UserCreationForm):
    """
    Form for creating a new user.

    Inherits from:
    - UserCreationForm: A built-in form for user creation.

    Attributes:
    - Meta: A nested class specifying metadata for the form.
        - model (User): The User model used for user creation.
        - fields (list): The fields included in the form (username, email, password1, password2).
    """
    class Meta:
        model=User
        fields=['username','email','password1','password2']




class StudentForm(ModelForm):
    """
    Form for handling student data.

    Inherits from:
    - ModelForm: A generic form for creating and updating model instances.

    Attributes:
    - Meta: A nested class specifying metadata for the form.
        - model (Student): The Student model used for the form.
        - fields (str): A special string value indicating that all fields of the model should be included in the form.
    """
    class Meta:
        model = Student
        fields='__all__'



class DepartmentForm(ModelForm):
    """
    Form for handling department data.

    Inherits from:
    - ModelForm: A generic form for creating and updating model instances.

    Attributes:
    - Meta: A nested class specifying metadata for the form.
        - model (Department): The Department model used for the form.
        - fields (str): A special string value indicating that all fields of the model should be included in the form.
    """
    class Meta:
        model = Department
        fields = '__all__'