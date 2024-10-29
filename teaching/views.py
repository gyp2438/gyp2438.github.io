from django.shortcuts import render
import time
from github_io.utils import get_sort
from django.db.models import OuterRef, Subquery
from cv.models import Employment
from home.models import Location
from .models import Course

# Create your views here.


def teaching_index(request):
    """
    main cv page

    Args:
        request (_type_): _description_
    """
    # courses = get_sort(Course, 'date')
    # Example with select_related for foreign key
    # courses = Course.objects.select_related('reading').all()
    # courses = get_sort(Course, 'date')
    # Adjust 'course_set' based on your related_name if you set one
    latest_experience_date = Employment.objects.filter(
        location=OuterRef('pk')).order_by('-from_date')

    locations = Location.objects.annotate(
        latest_experience_date=Subquery(
            latest_experience_date.values('from_date')[:1])
    ).order_by('latest_experience_date').prefetch_related('course')

    context = {'locations': locations}

    return render(request, "teaching/index.html", context)


def course_index(request, pk):
    """
    main cv page

    Args:
        request (_type_): _description_
    """

    course = Course.objects.get(pk=pk)

    context = {
        "course": course,
    }

    # populate course descriptions and stuff
    return render(request, "teaching/course_index.html", context)
