from django.contrib import admin
from . import models
# Register your models here.
@admin.action(description='Mark selected Posts as published')
def mark_posts_as_published(modeladmin, request, queryset):
    queryset.update(status='published')

@admin.action(description='Mark selected comments as active')
def mark_comments_as_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    actions = [mark_posts_as_published]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'is_active')
    search_fields = ('post__title', 'author__username', 'comment')
    list_filter = ('is_active', 'created_at')
    actions = [mark_comments_as_active]

admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Post, PostAdmin)
