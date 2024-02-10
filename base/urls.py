from django.urls import path
from . import views
urlpatterns = [

   path('home/',views.home,name="home"),

   path('',views.common_page,name="common_page"),
   path('login/',views.login_admin,name="login"),
   path('register/',views.register,name="register"),
   path('logout/',views.logout_user,name="logout"),

   path('student_info/<str:pk>/',views.studentinfo,name="student_info"),
   path('create_student/',views.create_student,name="create_student"),
]