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
        UserCreationForm (django.contrib.auth.forms)

    Attributes:
        username (CharField): The desired username for the new user.
        email (EmailField): The email address of the new user.
        password1 (CharField): The password for the new user.
        password2 (CharField): Confirmation of the password.

    Meta:
        model (User): The user model associated with the form.
        fields (list): The fields to include in the form.

    Example:
        form = CreateUserForm(data={'username': 'john_doe', 'email': 'john@example.com', 'password1': 'secure123', 'password2': 'secure123'})
        if form.is_valid():
            user = form.save()
    """
    class Meta:
        model=User
        fields=['username','email','password1','password2']


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
