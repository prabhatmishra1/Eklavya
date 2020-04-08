from django.contrib import admin
from Landingapp.models import Teacher
from django.contrib.auth.models import Group,User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
admin.site.register(Teacher)
admin.site.unregister(Group)
