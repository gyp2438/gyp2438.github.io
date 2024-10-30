from django.db import models

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


class Location(models.Model):
    name = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name
