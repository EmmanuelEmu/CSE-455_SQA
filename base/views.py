from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout



def common_page(request):
    """
    View for rendering the common page.

    Parameters:
    - request: HTTP request object.

    Returns:
    - HttpResponse: Rendered response for the common page.
    """
    return render(request,'base/common_page.html')



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
    std=Student.objects.all().order_by('-id')
    regular_std=Student.objects.filter(status='Regular').order_by('-id')[:10]
    #all_teacher=Teacher.objects.all()
    #top_10_dept=Department.objects.order_by('-id')[:10]
    #total_teacher=all_teacher.count()
    total_std=std.count()
    #total_dept=all_dept.count()
    context={'std':std,'regular_std':regular_std,'total_std':total_std}
    return render( request,'base/home.html',context)


def create_teacher(request):
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



def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'base/create_teacher.html', {'form': form})

def create_student(request):
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



def studentinfo(request,pk):
    student=Student.objects.get(id=pk)
    context={'student':student}
    return render(request,'base/student_info.html',context)





def nav_stu_list(request):

    """
    Display a list of students with filtering options.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered HTML page displaying the student list.

    Usage:
    This function is intended to be used as a Django view to display and filter a list of students.


    Sphinx Tags:
    - :param request: The HTTP request object.
    - :return: Rendered HTML page displaying the student list.

    Dependencies:
    - Django must be properly installed in the project.
    - StudentFilter class should be defined in the current module or imported.

    Notes:
    The function fetches all students from the database , order them by ID in descending order and applies filtering  based on the request
    parameters using the StudentFilter, counts the total number of students and renders the result in the
    'base/nav_stu_list.html' template.

    """

    students=Student.objects.all().order_by('-id')

    myFilter=StudentFilter(request.GET, queryset=students)
    students=myFilter.qs
    total_std=students.count()

    context={'myFilter':myFilter,'students':students,'total_std':total_std,'title': 'Students'}
    return render(request,'base/nav_stu_list.html',context)





def delete_student(request,pk):
    """
    Function to delete a student record.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - pk (int): Primary key of the student record to be deleted.

    Returns:
    HttpResponse: Redirects to the 'home' view after successful deletion.

    Usage:
    This function is intended to be used as a Django view to delete a specific student record.

    Sphinx Tags:
    - :param request: The HTTP request object.
    - :param pk: Primary key of the student record to be deleted.
    - :return: Redirects to the 'home' view after successful deletion.


    Dependencies:
    - Django must be properly installed in the project.



    Notes:
    The function fetches the student record with the provided primary key, handles the deletion
    upon receiving a POST request and redirects to the 'home' view after successful deletion.

    """


    item=Student.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    context={'item':item,'func':'delete_std'}
    return render(request,'base/delete.html',context)

