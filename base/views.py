from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout


    
def create_department(request):
    """
    View function to create a new department.

    This function handles both GET and POST requests. For GET requests,
    it renders a form to create a new department. For POST requests,
    it validates the form data and saves the new department if the form
    is valid.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: A response to the request. 
    """
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_department')
    else:
        form = DepartmentForm()
    return render(request, 'base/create_department.html', {'form': form})

