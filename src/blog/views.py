from django.shortcuts import render, get_object_or_404

from .models import Post
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


# def index(request):
#     posts = Post.objects.all()
#     return render(request, "index.html", {"posts": posts})
def blog_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,2)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    return render(request, 'index.html', {'posts': posts})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug, status="CR")
    return render(request,
                  'details.html',
                  {'post': post})
