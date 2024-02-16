from django.urls import path
from . import views
urlpatterns = [

    # URL for the common_page view
   path('',views.common_page,name="common_page"),
   # URL for the login_admin view
   path('login/',views.login_admin,name="login"),
   # URL for the register view
   path('register/',views.register,name="register"),
   # URL for the home view
   path('home/',views.home,name="home"),
   # URL for the create_notice view
   path('create_notice/',views.create_notice,name="create_notice"),
    # URL for the notice_details view with a dynamic parameter 'pk'
   path('notice_details/<str:pk>/',views.notice_details,name="notice_details"),
]