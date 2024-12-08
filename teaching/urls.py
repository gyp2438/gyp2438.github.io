from django.urls import path
from django_distill import distill_path
from teaching.models import Course
from . import views

# TODO slugify paths


def get_all_course_slug():
    return ((course.slug,) for course in Course.objects.all())


urlpatterns = [
    path("teaching/", views.teaching_index, name="teaching_index"),
    path("course/<slug:slug>/", views.course_index, name="course_index"),
    path('homework/<int:homework_id>/download/',
         views.download_pdf, name='download_pdf'),
]

urlpatterns += [

    distill_path(
        'teaching/',
        views.teaching_index,
        name='teaching_index',
        distill_file='teaching/index.html'  # Home page as index.html
    ),


    # Detail page URL for blog posts, matches "post/<int:pk>/"
    distill_path(
        'course/<slug:slug>/',
        views.course_index,
        name='course_index',
        distill_func=get_all_course_slug,  # Supplies primary keys for each post
        # Generates "post/<pk>/index.html"
        distill_file='course/{0}/index.html'
    ),
]
