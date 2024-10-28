from django.urls import path
from django_distill import distill_path
from .models import Education

from . import views

# TODO slugify paths


# def get_all_blog_pks():
#     return ((post.pk,) for post in Education.objects.all())


urlpatterns = [
    path("cv/", views.cv_index, name="cv_index"),
]
