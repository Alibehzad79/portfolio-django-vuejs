from django.contrib import admin
from socials_app.models import Social, SocialItem

# Register your models here.


class SocialItemInline(admin.TabularInline):
    model = SocialItem
    extra = 3


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [SocialItemInline]
