from django.urls import path
from . import views
urlpatterns = [
   path('',views.common_page,name="common_page"),

   path('login/',views.login_admin,name="login"),

]