from django.db import models
from github_io.utils import markdown_to_html

from django.utils.text import slugify
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:  # Only set the slug if it's not already set
            slug = slugify(self.name)
            # Ensure uniqueness
            original_slug = slug
            count = 1
            while Tag.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)


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
    about_me = models.TextField(help_text="Markdown text enabled")
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
        return markdown_to_html(self.about_me)


class Banner(models.Model):
    # TODO  define page banners separately
    banner = models.ImageField(upload_to='photos/', blank=True, null=True)
    page = models.SlugField(max_length=50, unique=True, blank=True,
                            help_text="Enter the template name, e.g., 'home', 'about'")

    def __str__(self):
        return self.page

    # TODO link to specific page
    # course specific banners??
    # course_banner = models.ImageField(upload_to='photos/', blank=True, null=True)


class Location(models.Model):
    name = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name
