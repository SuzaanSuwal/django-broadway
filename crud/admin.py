from django.contrib import admin

from .models import ClassRoom, UserProfile, Student


admin.site.register(ClassRoom)
admin.site.register(UserProfile)
admin.site.register(Student)

