from django.forms import ModelForm
from .models import *
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields='__all__'