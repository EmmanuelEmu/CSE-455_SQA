from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout


def common_page(request):
    """
    View for rendering the common page.

    Parameters:
    - request: HTTP request object.

    Returns:
    - HttpResponse: Rendered response for the common page.
    """
    return render(request, 'base/common_page.html')


def register(request):
    """
    View for user registration.

    Parameters:
    - request: HTTP request object.

    Returns:
    - HttpResponse: Redirect to the login page(after successfull registration).
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account Created ' + username)
                return redirect('login')

        context = {'form': form}
        return render(request, 'base/register.html', context)


def login_admin(request):
    """
    View for administrator login.

    Parameters:
    - request: HTTP request object.

    Returns:
    - HttpResponse: Redirect to  home page(successfull).
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

    return render(request, 'base/login.html')


def logout_user(request):
    """
    View for user logout.

    Parameters:
    - request: HTTP request object.

    Returns:
    - HttpResponse: Redirects to the login page after user logout.
    """
    logout(request)
    return redirect('login')


def home(request):
    """
    View for rendering the home page.

    Parameters:
    - request: HTTP request object.

    Returns:
    - HttpResponse: Rendered response for the home page.
    """
    return render(request, 'base/home.html')



def create_student(request):
    """
    View for creating a new student.

    Parameters:
    - request: HTTP request object.

    Returns:
    - HttpResponse: Redirect to home. 
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully.')
            return redirect('home')  
        else:
            messages.error(request, 'Error creating student. Please check the form.')

    else:
        form = StudentForm()

    return render(request, 'base/create_student.html', {'form': form})



def create_department(request):
    """
    View for creating a new department.

    Parameters:
    - request: HTTP request object.

    Returns:
    - HttpResponse: redirect to home (successfull creation).
    """
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DepartmentForm()
    
    return render(request, 'base/create_department.html', {'form': form})




