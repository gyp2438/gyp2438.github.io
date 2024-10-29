from django.db import models
from home.models import Person, Location
# Create your models here.


class Reading(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True, db_index=True)

    schedule = models.CharField(max_length=60, blank=True)
    office_hour = models.CharField(max_length=60, blank=True)

    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name='course')

    instructor = models.ForeignKey(
        Person, on_delete=models.PROTECT, related_name='course')

    reading = models.ForeignKey(
        Reading, on_delete=models.PROTECT, related_name='course')

    def __str__(self):
        return self.title

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
