from django.urls import path
from . import views
urlpatterns = [
   path('',views.common_page,name="common_page")

]