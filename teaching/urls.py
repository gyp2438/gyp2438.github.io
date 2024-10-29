from django.urls import path
from django_distill import distill_path

from . import views

# TODO slugify paths

urlpatterns = [
    path("teaching/", views.teaching_index, name="teaching_index"),
    path("course/<int:pk>/", views.course_index, name="course_index"),
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
]
