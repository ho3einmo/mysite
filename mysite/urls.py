from django.contrib import admin
from django.urls import path, include
# This is the main URL configuration for the Django project.
urlpatterns = [
    path('', include('blog.urls')),  # Include the blog app's URLs
    path('admin/', admin.site.urls),
]
