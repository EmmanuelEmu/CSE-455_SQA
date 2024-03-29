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



class AdminNoticeForm(forms.ModelForm):
    """
    Form for creating or updating an administrative notice.

    Inherits from:
        ModelForm (django.forms)

    Meta:
        model (AdminNotice): The model associated with the form.
        fields (str or list): The fields to include in the form. Use '__all__' to include all fields.

    Example:
        form = AdminNoticeForm(data={'sender': 'Admin', 'receiver': 'John', 'subject': 'Important Update', 'body': 'Please read the latest announcement.'})
        if form.is_valid():
            notice = form.save()
    """
    class Meta:
        
        model = AdminNotice
        fields = '__all__' 











