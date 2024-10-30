from django.shortcuts import render
# Create your views here.


def home_index(request):
    context = {}
    return render(request, "home/index.html", context)
