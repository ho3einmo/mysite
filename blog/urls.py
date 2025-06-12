from django.urls import path
from . import views
app_name = 'blog'  # Define the app name for namespacing
urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),  # URL for user signup
    path('login', views.login_view, name='login'),  # URL for user login
    path('logout/', views.logout_view, name='logout'),  # URL for user logout
    path('tags/<slug:tags_slug>/', views.list, name='list_by_tag'),  # URL for listing posts by tag
    path('', views.list, name='list'),  # Include the blog app's URLs
    path('<slug:slug>/<int:year>/<int:month>/<int:day>/', views.detail, name='detail'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),  # URL for liking a post
]