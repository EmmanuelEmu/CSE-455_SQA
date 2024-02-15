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




def home(request):
     
    return render( request,'base/home.html')