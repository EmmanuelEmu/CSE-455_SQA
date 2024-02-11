from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request,'base/home.html')

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


def create_notice(request):
    if request.method == 'POST':
        form = AdminNoticeForm(request.POST)
        if form.is_valid():  
           notice = form.save()
           return redirect('home')
    else:
       form = AdminNoticeForm()

    return render(request, 'base/create_notice.html', {'form': form})


def notice_details(request,pk):
    notice = AdminNotice.objects.get(id=pk)
    context={'notice': notice}
    return render(request,'base/notice_details.html',context)