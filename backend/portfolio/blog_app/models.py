from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.db.models import Q
# Create your models here.

class ArticleManager(models.Manager):
    def get_search(self, search_input):
        lookup = (
            Q(title__contains=search_input) |
            Q(slug__contains=search_input) |
            Q(content__contains=search_input)
        )
        return super().get_queryset().filter(lookup, is_active=True).all().distinct()
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(help_text="article-title", unique=True)
    image = models.ImageField(upload_to="blog/images/")
    content = HTMLField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=False, auto_now_add=False)

    objects = ArticleManager()
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail_api", kwargs={"slug": self.slug})
