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
    teachers=dept.teacher_set.all()
    students = dept.student_set.filter().order_by('-id')
    total_teacher=teachers.count()
    total_student=students.count()
    #context={'dept':dept,'students':students,'total_student':total_student,'teachers':teachers,'total_teacher': total_teacher}
    return render(request,'base/department_info.html',context)
