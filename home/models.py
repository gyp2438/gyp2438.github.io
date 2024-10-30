from django.db import models
from django.utils.safestring import mark_safe
import markdown

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30)

    # class Meta:
    #     verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Person(models.Model):
    """used to store co-authors on papers/projects

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    name = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=60, blank=True)
    affiliation = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="person")

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name


class Me(models.Model):
    person = models.OneToOneField(
        Person, on_delete=models.PROTECT, blank=True, null=True)
    about_me = models.TextField()
    github = models.URLField(blank=True)
    logo = models.ImageField(upload_to='photos/', blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='photos/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Me"

    def __str__(self):
        return self.person.name

    def about_me_html(self):
        # Convert Markdown content to HTML
        html_about = markdown.markdown(self.about_me)
        return mark_safe(html_about)


class Banner(models.Model):
    # TODO  define page banners separately
    banner = models.ImageField(upload_to='photos/', blank=True, null=True)
    # TODO link to specific page
    # course specific banners??
    # course_banner = models.ImageField(upload_to='photos/', blank=True, null=True)


class Location(models.Model):
    name = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name
