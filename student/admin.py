from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'stream', 'locked']
    list_filter = ['stream', 'courses', 'locked']
    search_fields = ['roll_no', 'name', 'stream', 'address', 'contact_number']

admin.site.register(Student, StudentAdmin)
