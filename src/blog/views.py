from django.shortcuts import render

from .models import Post
from django.views.generic import ListView, DetailView


# def index(request):
#     posts = Post.objects.all()
#     return render(request, "index.html", {"posts": posts})
class BlogList(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
