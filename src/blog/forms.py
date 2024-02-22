from django import forms

from . import models
from .models import Post


class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'created', 'updated', 'author']  # Exclude author field from form

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = Post.STATUS_CHOICES # Set choices for status field
