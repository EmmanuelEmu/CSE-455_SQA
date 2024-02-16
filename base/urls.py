from django.urls import path
from . import views

'''
URL Patterns
============

.. currentmodule:: myapp.urls

department_info
---------------

URL Pattern: ``department_info/<str:pk>/``

View: :func:`~myapp.views.department_info`

    This URL pattern is associated with the ``department_info`` view function. It expects a string parameter ``pk`` in the URL, which represents the primary key of the department.

``<str:pk>``: Represents a string parameter in the URL, where ``pk`` is the primary key of the department.

``views.department_info``: Refers to the view function responsible for handling requests to this URL pattern.
'''
urlpatterns = [
     path('department_info/<str:pk>/',views.department_info,name="department_info"),
]