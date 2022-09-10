
from django.contrib import admin
# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import StudentUser

admin.site.register(StudentUser, UserAdmin)