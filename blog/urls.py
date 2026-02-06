from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="blog_index"),
    path("category/<slug:slug>", views.blog_by_category, name="blog_by_category"),
    path("<slug:slug>", views.blog_details, name="blog_details"),
]
