from django.db import models

# Create your models here.

# TODO move person and location to a base model?


class Person(models.Model):
    """used to store co-authors on papers/projects

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    name = models.CharField(max_length=60)
    affiliation = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Education(models.Model):
    title = models.CharField(max_length=60)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="education")

    # location = models.CharField(max_length=60)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.title


class Employment(models.Model):
    role = models.CharField(max_length=60)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="employment")

    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f'{self.role}@{self.location}'


class Publication(models.Model):

    title = models.CharField(max_length=60)
    journal = models.CharField(max_length=60)
    pub_date = models.DateField()
    note = models.CharField(max_length=120, blank=True)
    people = models.ForeignKey(
        "Person", on_delete=models.PROTECT, related_name="publications")

    def __str__(self):
        return self.title


class Preprint(models.Model):
    title = models.CharField(max_length=60)
    status = models.DateField(max_length=30)
    note = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name


class Teaching(models.Model):
    role = models.CharField(max_length=60)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="teaching")

    def __str__(self):
        return self.name


class Mentoring(models.Model):
    title = models.CharField(max_length=120)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="mentoring")

    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.title


class Talk(models.Model):
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="talk")
    title = models.CharField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return self.title


class Service(models.Model):
    role = models.CharField(max_length=120)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="service")
    date = models.DateField()

    def __str__(self):
        return self.role


class Conference(models.Model):
    name = models.CharField(max_length=60)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="conference")
    date = models.DateField()

    def __str__(self):
        return self.name
