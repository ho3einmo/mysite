from django import template
from ..models import Post, Comment
register = template.Library()

@register.simple_tag
def total_posts():
    """
    Returns the total number of published posts.
    """
    return Post.objects.filter(status='published').count()

@register.simple_tag
def tag_or_tags(tag_count):
    if tag_count == 1:
        return "tag"
    else:
        return "tags"

@register.simple_tag
def total_comments(Post):
    return Comment.objects.filter(post=Post,is_active=True).count()