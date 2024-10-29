from django.db import models
from django.utils.safestring import mark_safe
import markdown
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
    affiliation = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="person")

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
    to_date = models.DateField(null=True, blank=True)

    def formatted_end_date(self):
        return self.to_date.strftime("%b %Y") if self.to_date else "Present"

    def __str__(self):
        return self.title


class Employment(models.Model):
    role = models.CharField(max_length=60)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="employment")

    from_date = models.DateField()

    to_date = models.DateField(null=True, blank=True)

    # markdown
    note = models.TextField(blank=True)

    def note_as_html(self):
        # Convert Markdown content to HTML
        html_note = markdown.markdown(self.note)
        return mark_safe(html_note)

    def formatted_end_date(self):
        return self.to_date.strftime("%b %Y") if self.to_date else "Present"

    def __str__(self):
        return f'{self.role}@{self.location}'


class Publication(models.Model):

    title = models.CharField(max_length=60)
    journal = models.CharField(max_length=60, blank=True)
    pub_date = models.DateField(blank=True, null=True)
    article = models.CharField(max_length=120, blank=True)
    volume = models.CharField(max_length=120, blank=True)
    issue = models.CharField(max_length=120, blank=True)
    people = models.ManyToManyField(
        "Person",  related_name="publications")
    doi = models.CharField(max_length=120, blank=True)

    def authors(self):
        author_list = self.people.all()  # Fetch all related authors
        n_auths = author_list.count()
        if n_auths == 0:
            return 'No authors'
        elif n_auths == 1:
            return author_list[0].name

        # Build the authors' string
        auths = ', '.join(person.name for person in author_list[:-1])
        auths += f' and {author_list.last().name}'
        return auths

    def formatted_end_date(self):
        return self.pub_date.strftime("%Y") if self.pub_date else "In Progress"

    def bib(self):
        # Start with the authors, followed by the year in parentheses
        citation = f"<b>{self.title}</b>. {
            self.authors()}, {self.formatted_end_date()}"

        if self.journal:
            citation += f", <i>{self.journal}</i>"
        if self.volume:
            citation += f", {self.volume}"
        if self.issue:
            citation += f", Issue {self.issue}"
        if self.article:
            citation += f" ({self.article})"
        if self.doi:
            citation += f'. <a href="{self.doi}" target="_blank">{self.doi}</a>'

        citation += "."
        return citation

    def __str__(self):
        return self.title


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

    to_date = models.DateField(null=True, blank=True)

    def formatted_end_date(self):
        return self.to_date.strftime("%b %Y") if self.to_date else "Present"

    def __str__(self):
        return self.title


class Talk(models.Model):
    # TODO needs multiple locations/dates
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class TalkDetail(models.Model):
    talk = models.ForeignKey(
        Talk, on_delete=models.PROTECT, related_name='details')

    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="details")
    date = models.DateField()
    note = models.TextField(max_length=60, blank=True)

    def formatted_end_date(self):
        return self.date.strftime("%b %Y")

    def __str__(self):
        return f"{self.talk.title}@{self.location.name[:10]}"


class Service(models.Model):
    role = models.CharField(max_length=120)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="service")
    date = models.DateField()

    def formatted_end_date(self):
        return self.date.strftime("%b %Y")

    def __str__(self):
        return self.role


class Conference(models.Model):
    name = models.CharField(max_length=60)
    location = models.ForeignKey(
        "Location", on_delete=models.PROTECT, related_name="conference")
    date = models.DateField()

    def formatted_end_date(self):
        return self.date.strftime("%b %Y")

    def __str__(self):
        return self.name
