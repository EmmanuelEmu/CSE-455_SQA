from django.urls import path
from . import views

""".. function:: path(route, view, kwargs=None, name=None)

   Defines a URL pattern to match the given route and view function.

   :param str route: The URL pattern to match. It may contain angle brackets to capture parameters.
   :param view: The view function to call when the URL pattern is matched.
   :type view: function or str
   :param dict kwargs: Optional keyword arguments to pass to the view function.
   :param str name: Optional name for the URL pattern.

   :returns: URL pattern for the specified route and view.
   :rtype: django.urls.path

.. function:: views.teacher_info(request, pk)

   View function to display information about a specific teacher.

   :param HttpRequest request: The HTTP request object.
   :param str pk: The primary key of the teacher to display information about.

   :returns: HTTP response displaying information about the teacher.
   :rtype: django.http.HttpResponse

.. function:: path('teacher_info/<str:pk>/', views.teacher_info, name="teacher_info")

   Defines a URL pattern for displaying information about a specific teacher.

   :param str pk: The primary key of the teacher to display information about.

   :returns: URL pattern for the teacher information view.
   :rtype: django.urls.path
"""

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



   path('',views.common_page,name="common_page"),
   path('login/',views.login_admin,name="login"),
   path('register/',views.register,name="register"),
   path('logout/',views.logout_user,name="logout"),


   path('home/',views.home,name="home"),


   path('student_info/<str:pk>/',views.student_info,name="student_info"),
   path('create_student/',views.create_student,name="create_student"),
   path('update_student/<str:pk>/',views.update_student,name="update_student"),
   path('delete_student/<str:pk>/',views.delete_student,name="delete_student"),
    path('create_teacher/',views.create_teacher,name="create_teacher"),
    path('teacher_info/<str:pk>/',views.teacher_info,name="teacher_info"),
    path('update_teacher/<str:pk>/',views.update_teacher,name="update_teacher"),


   path('nav_stu_list/',views.nav_stu_list,name="nav_stu_list"),


   path('department_info/<str:pk>/',views.department_info,name="department_info"),
   path('create_department/',views.create_department,name="create_department"),
   path('update_department/<str:pk>/',views.update_department,name="update_department"),

   path('create_notice/',views.create_notice,name="create_notice"),
   # URL for the update_notice view with a dynamic parameter 'pk'
   path('update_notice/<str:pk>/',views.update_notice,name="update_notice"),
   # URL for the notice_details view with a dynamic parameter 'pk'
   path('notice_details/<str:pk>/',views.notice_details,name="notice_details"),


]