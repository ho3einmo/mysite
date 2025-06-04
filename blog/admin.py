from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(models.Post, PostAdmin)