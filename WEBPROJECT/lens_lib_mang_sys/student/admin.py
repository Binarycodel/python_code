from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StudentUser, ElectronicBook
# Register your models here.

admin.site.register(StudentUser)
admin.site.register(ElectronicBook)