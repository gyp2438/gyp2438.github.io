from django.utils import timezone
from django.shortcuts import render
from django.db.models import OuterRef, Subquery

from cv.models import Education, Publication, Employment, Talk
from teaching.models import Course
from home.models import Location
from github_io.utils import get_sort, get_last_update
# Create your views here.


def cv_index(request):
    """
    main cv page

    Args:
        request (_type_): _description_
    """
    # minus sign -> descending -> most recent first

    latest_experience_date = Employment.objects.filter(
        location=OuterRef('pk')).order_by('-from_date')

    educations = get_sort(Education, 'to_date')
    employments = get_sort(Employment, 'to_date')
    publications = get_sort(Publication, 'pub_date')
    talks = get_sort(Talk, 'title')

    course_locations = Location.objects.annotate(
        latest_experience_date=Subquery(
            latest_experience_date.values('from_date')[:1])
    ).filter(course__isnull=False).order_by('latest_experience_date').prefetch_related('course')

    context = {
        "educations": educations,
        "employments": employments,
        "publications": publications,
        'talks': talks,
        'course_locations': course_locations,
        'last_update': get_last_update()
    }

    # TODO add other sections
    return render(request, "cv/index.html", context)
