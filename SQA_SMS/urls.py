from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    # URL pattern for accessing the Django admin interface
    path('admin/', admin.site.urls),
    # Include URL patterns from the 'base' app
    path('',include('base.urls')),
]
