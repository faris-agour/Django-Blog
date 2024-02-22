from django.urls import path

from . import views

app_name = 'blog'  # {% url 'blog:index'%} used for this
urlpatterns = [
    path("", views.blog_list, name='index'),
    path('post/<slug:slug>/', views.post_details, name='details'),
    path('add-post/', views.add, name='add'),
]
