from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout

def department_info(request,pk):
    dept=Department.objects.get(id=pk)
    context={'dept':dept}
    return render(request,'base/department_info.html',context)
