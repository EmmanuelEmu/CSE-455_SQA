from django.urls import path
from . import views
urlpatterns = [

   path('home/',views.home,name="home"),

   path('',views.common_page,name="common_page"),
   path('create_student/',views.create_student,name="create_student"),
]