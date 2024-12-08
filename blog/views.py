from django.views.generic import DetailView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from blog.forms import CommentForm
from blog.models import Post, Comment
from cv.models import Publication
from home.models import Banner
from github_io.utils import get_sort, get_last_update


# Create your views here.
# TODO slugify urls


def blog_index(request):
    """
    Gets all available blog posts to be sent to the view

    Args:
        request (_type_): _description_
    """
    banner = Banner.objects.filter(page='blog').first()

    # minus sign -> descending -> most recent first
    posts = Post.objects.all().order_by('-created_on')
    # TODO include all publications
    context = {
        "posts": posts,
        "title": "research",
        'banner': banner,
        'last_update': get_last_update()
    }
    return render(request, "blog/index.html", context)


def blog_detail(request, slug):
    """
    Get a specifc blog entry by primary key (pk)

    Args:
        request (_type_): _description_
        key (_type_): _description_
    """
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)

    banner = Banner.objects.filter(page=f'post-{slug}').first()
    if not banner:
        banner = Banner.objects.filter(page='blog').first()

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form": form,
        'banner': banner,

        'last_update': get_last_update()
    }

    return render(request, "blog/detail.html", context)
