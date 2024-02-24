from django.urls import path
from . import views
urlpatterns = [
   # URL for the home view
   path('home/',views.home,name="home"),
   # URL for the common page
   path('',views.common_page,name="common_page"),
   # URL for the student info
   path('student_info/<str:pk>/',views.studentinfo,name="student_info"),
   # URL for the create student
   path('create_student/',views.create_student,name="create_student"),
   # URL for the update student
   path('update_student/<str:pk>/',views.update_student,name="update_student"),
]