from django.db import models
from django.utils.text import slugify
from github_io.utils import markdown_to_html

from home.models import Person, Location, Me

# Create your models here.


class Reading(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Course(models.Model):
    # e.g. calculus 2
    title = models.CharField(max_length=120, help_text='e.g. Calculus')

    identifier = models.CharField(
        max_length=60, blank=True, help_text='e.g. Math132')
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True, db_index=True)

    schedule = models.CharField(max_length=60, blank=True)
    office_hour = models.CharField(max_length=60, blank=True)

    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name='course')

    instructor = models.ForeignKey(
        Person, on_delete=models.PROTECT, related_name='course', default=1)

    reading = models.ForeignKey(
        Reading, on_delete=models.PROTECT, related_name='course', blank=True, null=True, default=1)

    create_page = models.BooleanField(default=True)

    slug = models.SlugField(max_length=200, unique=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    url = models.URLField(blank=True)


    def course_id_html(self):
        # Convert Markdown content to HTML
        return markdown_to_html(self.identifier)
    

    def description_as_html(self):
        # Convert Markdown content to HTML
        return markdown_to_html(self.description)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Only set the slug if it's not already set
            slug = slugify(
                f'{self.season()[:2]}{self.year()[2:]} {self.identifier} {self.title}')
            # Ensure uniqueness
            original_slug = slug
            count = 1
            while Course.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def year(self):
        return self.date.strftime("%Y")

    def season(self):
        month = self.date.month
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        elif month in [9, 10, 11]:
            return "Fall"


class Homework(models.Model):
    name = models.CharField(max_length=60, blank=True)
    due_date = models.DateField()
    course = models.ManyToManyField(
        Course, related_name='homework')
    last_updated = models.DateTimeField(auto_now=True)

    pdf = models.FileField(
        upload_to="homeworks/pdfs/", null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
