from django.contrib import admin
from services_app.models import Service, ServiceOption, ServicePlan, RequestToWork

# Register your models here.


class ServiceOptionInline(admin.TabularInline):
    model = ServiceOption
    extra = 3


class ServicePlanInline(admin.TabularInline):
    model = ServicePlan
    extra = 3


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    inlines = [ServiceOptionInline, ServicePlanInline]


@admin.register(RequestToWork)
class RequestToWorkAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "date_recive")
    list_filter = ("date_recive",)
    search_fields = ("name", "email")
