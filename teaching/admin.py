from django.contrib import admin
from .models import Reading, Course, Homework

# Register your models here.


class ReadingAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    pass


class HomeworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Homework, HomeworkAdmin)
