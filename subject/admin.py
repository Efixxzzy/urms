from django.contrib import admin
from .models import *

# Register your models here.
class StreamAdmin(admin.ModelAdmin):
    list_display = ['branch', 'semester']
    list_filter = ['branch', 'semester']
    search_fields = ['branch', 'semester']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'stream', 'type']
    list_filter = ['stream', 'courses_offerred', 'type']
    search_fields = ['code', 'stream', 'courses_offerred', 'type']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'credits', 'stream']
    list_filter = ['stream', 'credits']
    search_fields = ['code', 'title', 'credits', 'stream']

admin.site.register(Stream, StreamAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)

