from django.contrib import admin
from .models import UserProfile


# Register your models here.


class AdminProfile(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(UserProfile, AdminProfile,)
