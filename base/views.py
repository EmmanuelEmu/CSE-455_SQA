from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
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


from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout



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
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DepartmentForm()
    return render(request, 'base/create_department.html', {'form': form})


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



def home(request):
     
    return render( request,'base/home.html')
