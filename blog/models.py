from django.db import models
from home.models import Tag
from github_io.utils import markdown_to_html

from django.utils.text import slugify


class Post(models.Model):
    """
    Defines the post with a title, body and tags 

    Args:
        models (_type_): _description_
    """
    title = models.CharField(max_length=255)
    body = models.TextField(help_text="Markdown Enabled.")
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=200, unique=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name="posts")

    def body_html(self):
        return markdown_to_html(self.body)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Only set the slug if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # if Post is deleted, also delete the comments
    # ForeignKeys are many to one - many comments for 1 post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} on {self.post}'
