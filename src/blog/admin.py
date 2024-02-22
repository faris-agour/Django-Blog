from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.db import models

from .models import Post, Comment




class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})},  # Use CKEditor for rich text editing
    }


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['content']
