from django.urls import path
from . import views
urlpatterns = [



   path('',views.common_page,name="common_page"),
   path('login/',views.login_admin,name="login"),
   path('register/',views.register,name="register"),
   path('create_notice/',views.create_notice,name="create_notice"),
]