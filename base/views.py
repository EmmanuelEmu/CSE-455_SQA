from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout

"""
.. module:: base.views
   :synopsis: Views for the base app.

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
   """

def create_department(request):
    """
    View function to create a new department.

    This function handles both GET and POST requests. For GET requests,
    it renders a form to create a new department. For POST requests,
    it validates the form data and saves the new department if the form
    is valid.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A response to the request. 
    """
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_department')
    else:
        form = DepartmentForm()
    return render(request, 'base/create_department.html', {'form': form})

"""

department_info
---------------

.. function:: department_info(request, pk)

   View function to retrieve and display department information.

   :param request: An object representing the request.
   :type request: HttpRequest
   :param pk: The primary key of the department to retrieve.
   :type pk: int
   :return: A rendered HTML response displaying department information.
   :rtype: HttpResponse
   :raises Department.DoesNotExist: If the department with the given primary key does not exist.

"""

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


"""

update_department
-----------------

.. function:: update_department(request, pk)

   View function to update a department.

   :param request: An object representing the request.
   :type request: HttpRequest
   :param pk: The primary key of the department to update.
   :type pk: int
   :return: A rendered HTML response displaying the form to update the department.
   :rtype: HttpResponse

"""

def update_department(request, pk):
    """
    View function to update a department.

    Args:
        request: An object representing the request.
        pk: The primary key of the department to update.

    Returns:
        HttpResponse: A rendered HTML response displaying the form to update the department.
    """
    item = Department.objects.get(id=pk)
    form = DepartmentForm(instance=item)
    current_rank = item.rank

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=item)
        if form.is_valid():
            rank = form.cleaned_data['rank']
            if rank != current_rank and Department.objects.filter(rank=rank).exists():
                messages.info(request, 'Already exists a dept with this Rank')
            else:
                form.save()
                return redirect('create_department')

    context = {'form': form}
    return render(request, 'base/create_department.html', context)
