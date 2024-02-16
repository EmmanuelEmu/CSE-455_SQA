from django.urls import path
from . import views

    
""".. function:: path(route, view, name=None)

        Defines a URL pattern to match the given route and view function.

        :param str route: The URL pattern to match.
        :param view: The view function to call when the URL pattern is matched.
        :type view: function or str
        :param str name: Optional name for the URL pattern.

        :returns: URL pattern for the specified route and view.
        :rtype: django.urls.path

        .. _create-teacher-url:

        URL Pattern for Creating a Teacher
        -----------------------------------

        The following URL pattern maps requests to create a new teacher to the view function
        ``views.create_teacher``:

        .. code-block:: python

            from django.urls import path
            from . import views

            urlpatterns = [
                path('create_teacher/', views.create_teacher, name="create_teacher"),
            ]

        This URL pattern is used to create a new teacher. When a user visits the URL
        ``/create_teacher/``, it triggers the ``create_teacher`` view function, which is
        responsible for rendering the form to create a new teacher and handling form submission.

        For more information on Django URL patterns, see:
        `Django URL dispatcher documentation <https://docs.djangoproject.com/en/stable/topics/http/urls/>`_

"""

urlpatterns = [



   path('home/',views.home,name="home"),


   path('',views.common_page,name="common_page"),


   path('login/',views.login_admin,name="login"),
   path('register/',views.register,name="register"),
   path('logout/',views.logout_user,name="logout"),
   
   
    path('create_teacher/',views.create_teacher,name="create_teacher"), 
]