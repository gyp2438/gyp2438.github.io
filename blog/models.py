from django.db import models


class Tag(models.Model):
    name = models.CharField(max_len=30)


class Post(models.Model):
    """
    Defines the post with a title, body and tags 

    Args:
        models (_type_): _description_
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField("Tag", related_name="posts")
