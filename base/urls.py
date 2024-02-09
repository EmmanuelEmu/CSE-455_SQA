from django.urls import path
from . import views
urlpatterns = [
   path('create_department/',views.create_department,name="create_department"),
]