from django.contrib import admin
from course.models import Department, Course
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "location")
    search_fields = ("title",)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'department')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
