from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField

from cv.models import Education, Publication, Employment, Talk

# Create your views here.
from django.db.models import Case, When, Value, IntegerField


def get_sort(model, date_field_name, descending=True):
    desc = ''
    if descending:
        desc = '-'

    return model.objects.annotate(
        is_in_progress=Case(
            # Check if the date field is None
            When(**{date_field_name: None}, then=Value(1)),
            default=Value(0),                                 # Default case
            output_field=IntegerField(),
        )
        # Sort by in-progress first, then by date
    ).order_by('-is_in_progress', desc + date_field_name)


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
    }

    # TODO add other sections
    return render(request, "cv/index.html", context)
