from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(('draft', 'Draft'), ('published', 'Published')), default='draft')
