from django.urls import path
from . import views
urlpatterns = [



   path('home/',views.home,name="home"),


   path('',views.common_page,name="common_page"),


   path('login/',views.login_admin,name="login"),
   path('register/',views.register,name="register"),
   path('logout/',views.logout_user,name="logout"),
   
   
    path('create_teacher/',views.create_teacher,name="create_teacher"),
   path('update_teacher/<str:pk>/',views.update_teacher,name="update_teacher"),
   path('delete_teacher/<str:pk>/',views.delete_teacher,name="delete_teacher"),

   
]