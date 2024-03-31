from django.contrib import admin
from contacts_app.models import Contact, ContactInfo, Phone

# Register your models here.


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 3


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_dispaly = ("__str__",)
    inlines = [PhoneInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "is_read", "date_recive")
    list_filter = ("is_read", "date_recive")
    search_fields = ("name", "email", "subject")
    list_editable = ("is_read",)
