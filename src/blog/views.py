from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

from .models import Post


# def index(request):
#     posts = Post.objects.all()
#     return render(request, "index.html", {"posts": posts})
def blog_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get("page")
    paginated_posts = paginator.get_page(page_number)
    query = request.GET.get('q')
    if query:
        paginated_posts = all_posts.filter(Q(title__icontains=query) | Q(body__icontains=query))

    return render(request, 'index.html', {'posts': paginated_posts})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug, status="CR")
    post_tags = post.tags.all()
    similar_posts = Post.objects.filter(tags__in=post_tags).exclude(slug=slug).distinct()
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by("-same_tags", "-created")[:4]

    return render(request,
                  'details.html',
                  {'post': post, "similar_posts": similar_posts})
