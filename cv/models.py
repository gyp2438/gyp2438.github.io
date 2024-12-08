from django.db import models
from django.utils.safestring import mark_safe
from home.models import Person, Location, Tag, Me
from teaching.models import Course

import markdown

# Create your models here.

# TODO add a last updated to each model and print the most recent update on the footer of the CV page


class Education(models.Model):
    title = models.CharField(max_length=60)
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="education", blank=True)

    # location = models.CharField(max_length=60)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def formatted_end_date(self):
        return self.to_date.strftime("%b %Y") if self.to_date else "Present"

    def __str__(self):
        return self.title


class Employment(models.Model):
    role = models.CharField(max_length=60)
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="employment", blank=True)

    from_date = models.DateField()

    to_date = models.DateField(null=True, blank=True)

    # markdown
    note = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def note_as_html(self):
        # Convert Markdown content to HTML
        html_note = markdown.markdown(self.note)
        return mark_safe(html_note)

    def formatted_end_date(self):
        return self.to_date.strftime("%b %Y") if self.to_date else "Present"

    def __str__(self):
        return f'{self.role}@{self.location}'


class Publication(models.Model):

    title = models.CharField(max_length=180)
    journal = models.CharField(max_length=60, blank=True)
    pub_date = models.DateField(blank=True, null=True)
    article = models.CharField(max_length=120, blank=True)
    volume = models.CharField(max_length=120, blank=True)
    issue = models.CharField(max_length=120, blank=True)

    doi = models.CharField(max_length=120, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    tag = models.ManyToManyField(Tag,
                                 related_name='publications', blank=True, default=None)

    # TODO people need to be sorted properly
    people = models.ManyToManyField(
        Person,  related_name="publications", blank=True, through='PublicationPerson')
    
    def get_me_instance(self):
        return Me.objects.first()
    
    def authors(self):
        author_list = self.people.all()  # Fetch all related authors
        n_auths = author_list.count()
        if n_auths == 0:
            return 'No authors'
        elif n_auths == 1:
            return author_list[0].name

        # Build the authors' string
        auths = []
        for i, person in enumerate(author_list):
            if i < n_auths-1:
                if person.name == self.me_instance.person.name:
                    auths.append(
                        f'<u>{person.name}</u>')

                else:
                    auths.append(person.name)

        auths = ', '.join(auths)
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


class PublicationPerson(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()  # Field to specify order

    class Meta:
        ordering = ['order']  # Ensure the default ordering is by 'order'

    def __str__(self):
        return f"{self.person.name} in {self.publication.title} (Order: {self.order})"


class Mentoring(models.Model):
    title = models.CharField(max_length=120)
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="mentoring", blank=True)

    from_date = models.DateField()

    to_date = models.DateField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def formatted_end_date(self):
        return self.to_date.strftime("%b %Y") if self.to_date else "Present"

    def __str__(self):
        return self.title


class Talk(models.Model):
    # TODO needs multiple locations/dates
    title = models.CharField(max_length=120)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TalkDetail(models.Model):
    talk = models.ForeignKey(
        Talk, on_delete=models.PROTECT, related_name='details', blank=True)

    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="details", blank=True)
    date = models.DateField()
    note = models.TextField(max_length=60, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def formatted_end_date(self):
        return self.date.strftime("%b %Y")

    def __str__(self):
        return f"{self.talk.title}@{self.location.name[:10]}"


class Service(models.Model):
    role = models.CharField(max_length=120)
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="service", blank=True)
    date = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)

    def formatted_end_date(self):
        return self.date.strftime("%b %Y")

    def __str__(self):
        return self.role


class Conference(models.Model):
    name = models.CharField(max_length=60)
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="conference", blank=True)
    date = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)

    def formatted_end_date(self):
        return self.date.strftime("%b %Y")

    def __str__(self):
        return self.name
