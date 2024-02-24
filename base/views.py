from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout
from .forms import StudentForm



def common_page(request):

    """
    Render the common page.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HttpResponse object.
    """

    return render(request,'base/common_page.html')


def studentinfo(request,pk):

    """
    Render the student information page.

    Args:
        request: HttpRequest object.
        pk: Primary key of the student object.

    Returns:
        Rendered HttpResponse object.
    """

    student=Student.objects.get(id=pk)
    context={'student':student}
    return render(request,'base/student_info.html',context)


def create_student(request):
    """
    Render the form for creating a new student or process form submission.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HttpResponse object with the form or redirects to home page.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'base/create_student.html', {'form': form})

def update_student(request, pk):
    """
    View function to update a student record.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the student to be updated.

    Returns:
        HttpResponse: Renders the create_student.html template with the updated form.
                      If the form is valid, redirects to the 'home' URL.

    Raises:
        Http404: If the student with the given primary key does not exist.

    """
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'base/create_student.html', {'form': form, 'update_mode': True})

def home(request):
    """
    Render the home page.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HttpResponse object.
    """
     
    return render( request,'base/home.html')