from django.shortcuts import render, get_object_or_404
from home.models import Banner, Tag
# Create your views here.
from blog.models import Post


def home_index(request):
    banner = get_object_or_404(Banner, page='home')

    context = {'banner': banner}
    return render(request, "home/index.html", context)


def tag_index(request, slug):
    """
    Allow filter by tag

    Args:
        request (_type_): _description_
        tag (_type_): _description_
    """
    tag = get_object_or_404(Tag, slug=slug)

    posts = Post.objects.filter(tags__name__contains=tag)
    posts = posts.order_by('-created_on')
    # TODO include all publications with tag

    context = {
        "posts": posts,
        'title': tag,
    }

    return render(request, "home/tag_index.html", context)
