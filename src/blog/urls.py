from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.BlogList.as_view(), name='index'),
    # path("<int:post_id>", ),
]
