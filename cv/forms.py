# your_app/forms.py
from django import forms
from cv.models import PublicationPerson
from django.db import models


class PublicationPersonForm(forms.ModelForm):
    class Meta:
        model = PublicationPerson
        fields = ['person', 'order']  # Include the fields you want in the form

    def __init__(self, *args, publication=None, **kwargs):  # Accept the publication argument
        super().__init__(*args, **kwargs)

        if publication:
            # Calculate the current maximum order value for the given publication
            max_order = PublicationPerson.objects.filter(
                publication=publication).aggregate(models.Max('order'))['order__max']
            initial_order = (max_order or 0) + 1  # Set default to max + 1
            # Set the initial value for the order field
            self.fields['order'].initial = initial_order
