from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from base.models import *
from base.forms import *
from base.filters import *
from base.forms import *
from base.filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout

'''
create_department
-----------------

.. function:: create_department(request)

   View function to create a new department.

   This function handles both GET and POST requests. For GET requests,
   it renders a form to create a new department. For POST requests,
   it validates the form data and saves the new department if the form
   is valid.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response to the request.
   :rtype: HttpResponse
'''

'''
department_info(request, pk)
----------------------------

View function to retrieve and display department information.

Args:
    request (HttpRequest): An object representing the request.
    pk (int): The primary key of the department to retrieve.

Returns:
    HttpResponse: A rendered HTML response displaying department information.

Raises:
    Department.DoesNotExist: If the department with the given primary key does not exist.

'''


def common_page(request):

    return render(request,'base/common_page.html')



def create_teacher(request):
    """
    View function for creating a new teacher.

    This view function handles both GET and POST requests. When a GET request is received,
    it initializes a new instance of the TeacherForm. When a POST request is received with
    valid form data, it saves the form data to create a new teacher instance and redirects
    the user to the 'home' page.

    :param HttpRequest request: The HTTP request object.
    :returns: A redirect response to the 'home' page if form submission is successful,
              otherwise, a rendered HTML template displaying the form.
    :rtype: HttpResponseRedirect or HttpResponse

    """
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, 'base/create_teacher.html', {'form': form})

""" This is the views section for teacher info viewing"""
def teacher_info(request,pk):
    
    """
    View function to display information about a specific teacher.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the teacher to display information about.

    Returns:
        HttpResponse: A response displaying information about the teacher.
    """
    teacher=Teacher.objects.get(id=pk)
    context={'teacher':teacher}
    return render(request, 'base/teacher_info.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form= CreateUserForm()
 
        if request.method=='POST':
                form=CreateUserForm(request.POST)
                if form.is_valid():
                    user=form.save()
                    username=form.cleaned_data.get('username')
                    messages.success(request,'Account Created ' +username)
                    return redirect('login')
    

        context={'form':form}
        return render(request,'base/register.html',context)



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
            return redirect('home')
            return redirect('create_department')
    else:
        form = DepartmentForm()
    return render(request, 'base/create_department.html', {'form': form})

def department_info(request, pk):
    """
    View function to retrieve and display department information.

    Args:
        request: HttpRequest object representing the request.
        pk: Primary key of the department to retrieve.

    Returns:
        HttpResponse: Rendered HTML response displaying department information.

    Raises:
        Department.DoesNotExist: If the department with the given primary key does not exist.
    """
    dept = Department.objects.get(id=pk)
    context = {'dept': dept}
    return render(request, 'base/department_info.html', context)

def login_admin(request):

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
    logout(request)
    return redirect('login')
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
     
    return render( request,'base/home.html')

    """
    Render the home page.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HttpResponse object.
    """
     
    return render( request,'base/home.html')
