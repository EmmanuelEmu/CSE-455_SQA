from django.urls import path
from . import views
urlpatterns = [
     path('department_info/<str:pk>/',views.department_info,name="department_info"),
]