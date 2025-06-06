from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator
from . import forms
# Create your views here.
def list(request,tags_slug=None):
    if tags_slug:
        posts = models.Post.objects.filter(status='published', tags__slug=tags_slug).order_by('-created_at')
    else:
        posts = models.Post.objects.filter(status='published').order_by('-created_at')
    paginator = Paginator(posts, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/list.html', {'posts': posts})


def detail(request, slug, year, month, day):
    post = get_object_or_404(models.Post, created_at__year=year, created_at__month=month, created_at__day=day, slug=slug, status='published')
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.email = request.user.email
            comment.save()
            return render(request, 'blog/detail.html', {'post': post, 'comment_form': forms.CommentForm(), 'message': 'Your comment is awaiting approval.'})
    else:
        comment_form = forms.CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'comment_form': forms.CommentForm(), 'message': 'insert your comment below.'})