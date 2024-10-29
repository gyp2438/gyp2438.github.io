from django.urls import path
from django_distill import distill_path
from .models import Post, Tag
from . import views

# TODO slugify paths


def get_all_blog_pks():
    return ((post.pk,) for post in Post.objects.all())


def get_all_tags():
    return ((tag.name,) for tag in Tag.objects.all())


urlpatterns = [
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("tag/<tag>/", views.blog_tag, name="blog_tag"),
]


urlpatterns += [
    # Home page URL
    distill_path(
        'blog/',
        views.blog_index,
        name='blog_index',
        distill_file='index.html'  # Home page as index.html
    ),

    # Detail page URL for blog posts, matches "post/<int:pk>/"
    distill_path(
        'post/<int:pk>/',
        views.blog_detail,
        name='blog_detail',
        distill_func=get_all_blog_pks,  # Supplies primary keys for each post
        # Generates "post/<pk>/index.html"
        distill_file='post/{0}/index.html'
    ),

    # Tag page URL, matches "tag/<tag>/"
    distill_path(
        'tag/<tag>/',
        views.blog_tag,
        name='blog_tag',
        distill_func=get_all_tags,  # Supplies all unique tags
        # Generates "tag/<tag>/index.html"
        distill_file='tag/{0}/index.html'
    ),
]
