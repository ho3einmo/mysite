from django.urls import path
from . import views
app_name = 'blog'  # Define the app name for namespacing
urlpatterns = [
    path('tags/<slug:tags_slug>/', views.list, name='list_by_tag'),  # URL for listing posts by tag
    path('', views.list, name='list'),  # Include the blog app's URLs
    path('<slug:slug>/<int:year>/<int:month>/<int:day>/', views.detail, name='detail'),
]