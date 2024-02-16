from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout



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

    




def home(request):

    """
    Render the home page.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HttpResponse object.
    """
     
    return render( request,'base/home.html')