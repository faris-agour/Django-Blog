from django.contrib import admin

from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['content']
