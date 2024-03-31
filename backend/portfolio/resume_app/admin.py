from django.contrib import admin
from resume_app.models import Resume, Education, Experiance, Skill

# Register your models here.


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class ExperianceInline(admin.TabularInline):
    model = Experiance
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    inlines = [EducationInline, ExperianceInline, SkillInline]
