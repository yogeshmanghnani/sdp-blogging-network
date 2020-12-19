from django.contrib import admin
from .models import Profile, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
