from django.urls import path
from . import views
urlpatterns = [
    # URL for the home view
    path('home/', views.home, name="home"),

    # URL for the common_page view
    path('', views.common_page, name="common_page"),

    # URL for the studentinfo view with a dynamic parameter 'pk'
    path('student_info/<str:pk>/', views.studentinfo, name="student_info"),

    # URL for the create_student view
    path('create_student/', views.create_student, name="create_student"),
]