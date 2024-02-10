from django.urls import path
from . import views
urlpatterns = [



   path('',views.common_page,name="common_page"),
   path('login/',views.login_admin,name="login"),
   path('register/',views.register,name="register"),


   path('create_student/',views.create_student,name="create_student"),
]