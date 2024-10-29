from django.utils import timezone
from django.shortcuts import render

from cv.models import Education, Publication, Employment, Talk
from github_io.utils import get_sort, get_last_update
# Create your views here.


def cv_index(request):
    """
    main cv page

    Args:
        request (_type_): _description_
    """
    # minus sign -> descending -> most recent first
    educations = get_sort(Education, 'to_date')
    employments = get_sort(Employment, 'to_date')
    publications = get_sort(Publication, 'pub_date')
    talks = get_sort(Talk, 'title')

    context = {
        "educations": educations,
        "employments": employments,
        "publications": publications,
        'talks': talks,
        'last_update': get_last_update()
    }

    # TODO add other sections
    return render(request, "cv/index.html", context)
