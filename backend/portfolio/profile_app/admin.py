from django.contrib import admin
from profile_app.models import MyProfile

# Register your models here.


@admin.register(MyProfile)
class MyProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name",)
