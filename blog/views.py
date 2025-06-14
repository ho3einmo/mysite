from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.core.paginator import Paginator
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog:list')  # Redirect to the blog list after signup
    else:
        form = forms.SignUpForm()
    return render(request, 'blog/sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:list')
    else:
        form = forms.LoginForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('blog:list')

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
@login_required
def like_post(request, post_id):
    post = get_object_or_404(models.Post, id=post_id)
    like, created = models.Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        message = 'You unliked this post.'
    else:
        message = 'You liked this post.'
    return redirect('blog:detail', slug=post.slug, year=post.created_at.year, month=post.created_at.month, day=post.created_at.day)
