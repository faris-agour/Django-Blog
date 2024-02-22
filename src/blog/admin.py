from django.contrib import admin

from .models import Post, Comment
from django.db import models
from django import forms


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})},  # Use CKEditor for rich text editing
    }


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['content']
