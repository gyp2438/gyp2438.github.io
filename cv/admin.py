from django.contrib import admin
from cv.models import Education, Employment, Publication, \
    Teaching, Mentoring, Talk, TalkDetail, Service, Conference

# Register your models here.


class EducationAdmin(admin.ModelAdmin):
    pass


class EmploymentAdmin(admin.ModelAdmin):
    pass


class PublicationAdmin(admin.ModelAdmin):
    pass


class TeachingAdmin(admin.ModelAdmin):
    pass


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
admin.site.register(Teaching, TeachingAdmin)
admin.site.register(Mentoring, MentoringAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(TalkDetail, TalkDetailAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Service, ServiceAdmin)
