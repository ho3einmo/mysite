from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'is_active')
    search_fields = ('post__title', 'author__username', 'comment')
    list_filter = ('is_active', 'created_at')

admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Post, PostAdmin)
