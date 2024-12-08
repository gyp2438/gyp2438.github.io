from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import OuterRef, Subquery, Prefetch

from cv.models import Education, Publication, Employment, Talk, Conference,Service
from teaching.models import Course
from home.models import Location, Banner
from github_io.utils import get_sort, get_last_update
# Create your views here.


def cv_index(request):
    """
    main cv page

    Args:
        request (_type_): _description_
    """
    # minus sign -> descending -> most recent first
    banner = Banner.objects.filter(page='cv').first()
    educations = get_sort(Education, 'to_date')
    employments = get_sort(Employment, 'to_date')
    publications = get_sort(Publication, 'pub_date')
    talks = get_sort(Talk, 'title')
    services = get_sort(Service, 'date_end')

    conferences = get_sort(Conference, 'date')

    latest_experience_date = Employment.objects.filter(
        location=OuterRef('pk')).order_by('-from_date')

    # Replace 'your_field_here' with the field you want to sort by
    ordered_courses = Course.objects.order_by('-date')

    course_locations = Location.objects.annotate(
        latest_experience_date=Subquery(
            latest_experience_date.values('from_date')[:1])
    ).filter(course__isnull=False).order_by('latest_experience_date')
    course_locations = course_locations.prefetch_related(
        Prefetch('course', queryset=ordered_courses)).distinct()

    context = {
        "educations": educations,
        "employments": employments,
        "publications": publications,
        'talks': talks,
        'course_locations': course_locations,
        'banner': banner,
        'conferences': conferences,
        'services':services,
        'last_update': get_last_update()
    }

    # TODO add other sections
    return render(request, "cv/index.html", context)
