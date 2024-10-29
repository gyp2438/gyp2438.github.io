from django.contrib import admin
from .models import Person, Location

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Location, LocationAdmin)
