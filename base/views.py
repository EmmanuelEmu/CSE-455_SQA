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





def login_admin(request):

    if request.user.is_authenticated:
        return redirect('create_student')

    else:

       if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  
               
            else:
                messages.info(request, 'Username or Password is incorrect')

    return render(request, 'base/login.html')


def studentinfo(request,pk):
    student=Student.objects.get(id=pk)
    context={'student':student}
    return render(request,'base/student_info.html',context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = StudentForm()
    return render(request, 'base/create_student.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')



def home(request):
     
    return render( request,'base/home.html')