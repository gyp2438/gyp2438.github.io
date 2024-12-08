from django.contrib import admin
from cv.models import Education, Employment, Publication, \
    Mentoring, Talk, TalkDetail, Service, Conference, PublicationPerson

# Register your models here.


class EducationAdmin(admin.ModelAdmin):
    pass


class EmploymentAdmin(admin.ModelAdmin):
    pass


class PublicationPersonInline(admin.TabularInline):
    model = PublicationPerson
    extra = 1  # Number of empty forms to display
    fields = ('person', 'order')  # Fields to display in the inline
    ordering = ['order']  # Ensure inline is ordered by the 'order' field


class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationPersonInline]


class MentoringAdmin(admin.ModelAdmin):
    pass


class TalkAdmin(admin.ModelAdmin):
    pass


class TalkDetailAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass


class ConferenceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Education, EducationAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Mentoring, MentoringAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(TalkDetail, TalkDetailAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Service, ServiceAdmin)
