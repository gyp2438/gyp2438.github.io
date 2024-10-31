from django.shortcuts import render, get_object_or_404
from home.models import Banner
# Create your views here.


def home_index(request):
    banner = get_object_or_404(Banner, page='home')

    context = {'banner': banner}
    return render(request, "home/index.html", context)
