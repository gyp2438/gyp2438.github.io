from django.urls import path
from django_distill import distill_path
from .models import Post
from . import views

# TODO slugify paths


def get_all_blog_slug():
    return ((post.slug,) for post in Post.objects.all())


urlpatterns = [
    path("blog/", views.blog_index, name="blog_index"),
    path("post/<slug:slug>/", views.blog_detail, name="blog_detail"),
]


urlpatterns += [
    # Home page URL
    distill_path(
        'blog/',
        views.blog_index,
        name='blog_index',
        distill_file='blog/index.html'  # Home page as index.html
    ),

    # Detail page URL for blog posts, matches "post/<int:pk>/"
    distill_path(
        'post/<slug:slug>/',
        views.blog_detail,
        name='blog_detail',
        distill_func=get_all_blog_slug,  # Supplies primary keys for each post
        # Generates "post/<pk>/index.html"
        distill_file='post/{0}/index.html'
    ),

]
