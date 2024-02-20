from django.db.models import Count
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
    post_tags =post.tags.all()
    similar_posts = Post.objects.filter(tags__in=post_tags).exclude(slug=slug).distinct()
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by("-same_tags","-created")[:4]

    return render(request,
                  'details.html',
                  {'post': post, "similar_posts":similar_posts})
