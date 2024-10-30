from django.contrib import admin
from .models import Person, Location, Tag, Me

# Register your models here.


class MeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only allow adding if no Me instance exists
        return not Me.objects.exists()


class PersonAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Me, MeAdmin)
