from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import AddForm
from .models import Post


def blog_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get("page")
    paginated_posts = paginator.get_page(page_number)
    query = request.GET.get('q')
    if query:
        paginated_posts = all_posts.filter(
            Q(title__icontains=query) | Q(body__icontains=query) | Q(tags__name__icontains=query)).distinct()
    return render(request, 'index.html', {'posts': paginated_posts})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug, status="CR")
    post_tags = post.tags.all()
    similar_posts = Post.objects.filter(tags__in=post_tags).exclude(slug=slug).distinct()
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by("-same_tags", "-created")[:4]

    return render(request,
                  'details.html',
                  {'post': post, "similar_posts": similar_posts})


@login_required
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the current user
            post.save()
            form.save_m2m()  # Save many-to-many fields
            post_slug = post.slug  # Replace 'your-post-slug' with the actual slug of the post
            return redirect(reverse('blog:details', kwargs={'slug': post_slug}))  # Redirect to the post details page
    else:
        form = AddForm()

    return render(request, 'add.html', {'form': form})  # Return the form for GET requests
