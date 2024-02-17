from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.blog_list, name='index'),
    path('post/<slug:slug>/', views.post_details, name='details'),
]
