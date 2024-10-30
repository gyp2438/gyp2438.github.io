from django.shortcuts import render
from django.http import HttpResponseRedirect

from blog.forms import CommentForm
from blog.models import Post, Comment
from cv.models import Publication


# Create your views here.
# TODO slugify urls


def blog_index(request):
    """
    Gets all available blog posts to be sent to the view

    Args:
        request (_type_): _description_
    """
    # minus sign -> descending -> most recent first
    posts = Post.objects.all().order_by('-created_on')
    # TODO include all publications
    context = {
        "posts": posts,
        "title": "research"
    }
    return render(request, "blog/index.html", context)


def blog_tag(request, tag):
    """
    Allow filter by tag

    Args:
        request (_type_): _description_
        tag (_type_): _description_
    """
    posts = Post.objects.filter(tags__name__contains=tag)
    posts = posts.order_by('-created_on')
    # TODO include all publications with tag

    context = {
        "posts": posts,
        'title': tag,
    }

    return render(request, "blog/index.html", context)


def blog_detail(request, pk):
    """
    Get a specifc blog entry by primary key (pk)

    Args:
        request (_type_): _description_
        key (_type_): _description_
    """
    post = Post.objects.get(pk=pk)

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
    }

    return render(request, "blog/detail.html", context)
