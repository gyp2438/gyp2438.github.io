from django.shortcuts import render, get_object_or_404
from home.models import Banner, Tag
# Create your views here.
from blog.models import Post
from github_io.utils import get_sort, get_last_update


def home_index(request):
    # banner = get_object_or_404(Banner, page='home')

    # banner = Banner.objects.first()  # Use .first() to avoid exceptions
    

    banner = Banner.objects.filter().first()  # Use .first() to avoid exceptions
    if not banner:
        # Default banner data when no banner exists
        banner = {
            "banner": None,  # No image available
            "page": "home",
            "last_updated": None
        }

    context = {'banner': banner, 'last_update': get_last_update()}
    return render(request, "home/index.html", context)


def tag_index(request, slug):
    """
    Allow filter by tag

    Args:
        request (_type_): _description_
        tag (_type_): _description_
    """
    tag = get_object_or_404(Tag, slug=slug)
    banner = Banner.objects.filter(page=f'tag-{slug}').first()

    if not banner:
        banner = Banner.objects.filter(page='home').first()

    posts = Post.objects.filter(tags__name__contains=tag)
    posts = posts.order_by('-created_on')
    # TODO include all publications with tag

    context = {
        "posts": posts,
        'title': tag,
        'last_update': get_last_update(),
        'banner': banner,

    }

    return render(request, "home/tag_index.html", context)
