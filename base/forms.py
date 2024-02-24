from django.forms import ModelForm
from .models import *
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

'''


.. module:: base.models
   :synopsis: Models for the base app.

Department Model
----------------

.. autoclass:: base.models.Department
   :members:
   :undoc-members:
   :show-inheritance:

   Model representing a department in your organization.

   Attributes:
       name (str): The name of the department.
       location (str): The location of the department. Choices are 'Block A', 'Block B', 'Block C', 'Block D', 'Block E'.
       rank (int): The rank of the department.
       phone (str): The phone number of the department.
       email (str): The email address of the department.
       date_created (datetime): The date and time when the department was created.
       description (str): A description of the department.

   .. attribute:: LOCATION

      Choices for the department's location.

      .. code-block:: python

         (
             ('Block A', 'Block A'),
             ('Block B', 'Block B'),
             ('Block C', 'Block C'),
             ('Block D', 'Block D'),
             ('Block E', 'Block E'),
         )

   .. automethod:: __str__


DepartmentForm Form
-------------------

.. module:: base.forms
   :synopsis: Forms for the base app.

.. autoclass:: base.forms.DepartmentForm
   :members:
   :exclude-members: __weakref__

   Form for creating or updating a department.

   Inherits from Django's ModelForm.

   .. autoclass:: Meta
      :annotation: = base.forms.DepartmentForm.Meta
      :type: Meta

Meta
~~~~

.. autoclass:: base.forms.DepartmentForm.Meta
   :members:

   Meta class for DepartmentForm.

   Defines the model and fields to be used in the form.

'''


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