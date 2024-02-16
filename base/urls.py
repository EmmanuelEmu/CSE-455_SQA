from django.urls import path
from . import views
'''
URL Patterns
------------

The urlpatterns list in your Django application defines the mapping between URL paths and view functions. 

.. code-block:: python

   from django.urls import path
   from . import views

   urlpatterns = [
       path('create_department/', views.create_department, name="create_department"),
   ]

create_department
~~~~~~~~~~~~~~~~~

The ``create_department`` path is mapped to the ``views.create_department`` view function.

- URL Path: ``/create_department/``
- View Function: :func:`~.views.create_department`
- Name: ``create_department``

This URL allows users to create a new department.

'''
urlpatterns = [
   path('create_department/',views.create_department,name="create_department"),
]