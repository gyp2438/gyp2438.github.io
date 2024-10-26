from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    # class Meta:
    #     verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # if Post is deleted, also delete the comments
    # ForeignKeys are many to one - many comments for 1 post
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} on {self.post}'
