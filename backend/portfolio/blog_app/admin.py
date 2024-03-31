from django.contrib import admin
from blog_app.models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "date_created")
    list_editable = ("is_active",)
    list_filter = ("is_active", "date_created")
    search_fields = ("title", "slug", "content")
