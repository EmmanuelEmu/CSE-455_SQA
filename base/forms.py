from django.forms import ModelForm
from .models import *
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

'''
CreateUserForm
===============

.. autoclass:: yourapp.forms.CreateUserForm
   :members:
   :undoc-members:
   :show-inheritance:

   Form for creating a new user.

   Inherits from Django's UserCreationForm.

   .. autoclass:: Meta
      :members:
      :undoc-members:

      Meta class for CreateUserForm.

      Defines the model and fields to be used in the form.

DepartmentForm
==============

.. autoclass:: yourapp.forms.DepartmentForm
   :members:
   :undoc-members:
   :show-inheritance:

   Form for creating or updating a department.

   Inherits from Django's ModelForm.

   .. autoclass:: Meta
      :members:
      :undoc-members:

      Meta class for DepartmentForm.

      Defines the model and fields to be used in the form.

'''

class CreateUserForm(UserCreationForm):
    """
    Form for creating a new user.

    Inherits from Django's UserCreationForm.
    """
    class Meta:
        """
        Meta class for CreateUserForm.

        Defines the model and fields to be used in the form.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DepartmentForm(ModelForm):
    """
    Form for creating or updating a department.

    Inherits from Django's ModelForm.
    """
    class Meta:
        """
        Meta class for DepartmentForm.

        Defines the model and fields to be used in the form.
        """
        model = Department
        fields = '__all__'
