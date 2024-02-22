from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['content']
