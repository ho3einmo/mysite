from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator
# Create your views here.
def list(request):
    posts = models.Post.objects.filter(status='published').order_by('-created_at')
    paginator = Paginator(posts, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/list.html', {'posts': posts})


def detail(request, slug, year, month, day):
    post = get_object_or_404(models.Post, created_at__year=year, created_at__month=month, created_at__day=day, slug=slug, status='published')
    return render(request, 'blog/detail.html', {'post': post})