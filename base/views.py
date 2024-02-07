from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
# from .forms import *
# from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout


def login_admin(request):

    # if request.user.is_authenticated:
    #     return redirect('home')

    # else:

    #    if request.method == 'POST':
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')
    #         user = authenticate(request, username=username, password=password)

    #         if user is not None:
    #             login(request, user)  
    #             return redirect('home')
    #         else:
    #             messages.info(request, 'Username or Password is incorrect')

    return render(request, 'base/login.html')