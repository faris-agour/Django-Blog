from django.shortcuts import render, get_object_or_404

from .models import Post
from django.views.generic import ListView, DetailView


# def index(request):
#     posts = Post.objects.all()
#     return render(request, "index.html", {"posts": posts})
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug, status="CR")
    return render(request,
                  'details.html',
                  {'post': post})
