from django.contrib import admin
from projects_app.models import Project, Category, ProjectGallery

# Register your models here.


class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ProjectGalleryInline]


admin.site.register(Category)
