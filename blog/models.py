from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(('draft', 'Draft'), ('published', 'Published')), default='draft')
    tags = TaggableManager(blank=True)

    def __str__(self):
        return "{}-{}-{}".format(self.title, self.author.username, self.created_at.strftime('%Y-%m-%d %H:%M:%S'))
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={
            'slug': self.slug,
            'year': self.created_at.year,
            'month': self.created_at.month,
            'day': self.created_at.day
        })
    def active_comments(self):
        return self.comments.filter(is_active=True).order_by('-created_at')
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}-{}-{}".format(self.post.title, self.author, self.created_at.strftime('%Y-%m-%d %H:%M:%S'))
    
class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"