from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout




"""
create_department
-----------------

View function to create a new department.

This function handles both GET and POST requests. For GET requests, it renders a form to create a new department. 
For POST requests, it validates the form data and saves the new department if the form is valid.

Parameters:
    - ``request`` (HttpRequest): The HTTP request object.

Returns:
    - HttpResponse: A response to the request.

"""

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
   # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # If it's a POST request, create a form instance with the POST data
        form = DepartmentForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # If the form is valid, save the form data
            form.save()
            # Redirect to a success page or view
            return redirect('create_department')
    else:
        # If it's not a POST request, create an empty form instance
        form = DepartmentForm()
    
    # Render the template with the form (either with POST data or empty)
    return render(request, 'base/create_department.html', {'form': form})



"""
department_info
===============

View function to retrieve and display department information.

Parameters
----------
request : HttpRequest
    HttpRequest object representing the request.
pk : int
    Primary key of the department to retrieve.

Returns
-------
HttpResponse
    Rendered HTML response displaying department information.

Raises
------
Department.DoesNotExist
    If the department with the given primary key does not exist.

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
    # Retrieve the department object with the given primary key
    dept = Department.objects.get(id=pk)
    
    # Prepare the context dictionary with the department object
    context = {'dept': dept}
    
    # Render the template with the department information
    return render(request, 'base/department_info.html', context)




"""

Update Department
-----------------

View function to update a department.

Args:
    request (HttpRequest): The HTTP request object.
    pk (int): The primary key of the department to be updated.

Returns:
    HttpResponse: The HTTP response object rendering the template.

Details:
    This function retrieves a department object from the database based on the given primary key (`pk`).
    It then populates a form with the retrieved department data for updating.
    If the request method is POST, it validates the form data and saves the updated department if the form is valid.
    If the rank of the department is changed and a department with the new rank already exists, it displays a message.
    Finally, it renders the 'base/create_department.html' template with the form data.

Example::

    # Example usage:
    # To update a department with ID 1
    update_department(request, 1)
"""



def update_department(request, pk):
    """
    View function to update a department.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the department to be updated.

    Returns:
        HttpResponse: The HTTP response object rendering the template.

    """
    # Retrieve the department object to be updated
    item = Department.objects.get(id=pk)
    
    # Create a form instance with the retrieved department data
    form = DepartmentForm(instance=item)
    
    # Get the current rank of the department
    current_rank = item.rank

    if request.method == 'POST':
        # If the form is submitted, bind the data to the form
        form = DepartmentForm(request.POST, instance=item)
        if form.is_valid():
            # If the form data is valid, retrieve the rank from the form
            rank = form.cleaned_data['rank']
            
            # Check if the rank has been changed and if a department with the new rank already exists
            if rank != current_rank and Department.objects.filter(rank=rank).exists():
                # If a department with the new rank already exists, display a message
                messages.info(request, 'Already exists a department with this rank')
            else:
                # If the rank is valid and unique, save the form data
                form.save()
                # Redirect to a success page or view
                return redirect('create_department')

    # Render the template with the form
    context = {'form': form}
    return render(request, 'base/create_department.html', context)

