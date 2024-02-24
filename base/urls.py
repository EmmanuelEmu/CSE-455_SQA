from django.urls import path
from . import views

"""
URL Patterns
------------

This module defines the URL patterns for the application.

URL Patterns:
    - ``department_info/<str:pk>/``: This URL pattern maps to the ``department_info`` view function. It expects a string primary key (`pk`) as a parameter in the URL path.
    - ``create_department/``: This URL pattern maps to the ``create_department`` view function.
    - ``update_department/<str:pk>/``: This URL pattern maps to the ``update_department`` view function. It expects a string primary key (`pk`) as a parameter in the URL path.

"""
urlpatterns = [
     path('department_info/<str:pk>/',views.department_info,name="department_info"),
     path('create_department/',views.create_department,name="create_department"),
     path('update_department/<str:pk>/',views.update_department,name="update_department"),


]