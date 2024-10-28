from django.shortcuts import render
from cv.models import Education

# Create your views here.


def cv_index(request):
    """
    main cv page

    Args:
        request (_type_): _description_
    """
    # minus sign -> descending -> most recent first
    educations = Education.objects.all().order_by('-to_date')
    context = {
        "educations": educations,
    }

    # TODO add other sections
    return render(request, "cv/index.html", context)
