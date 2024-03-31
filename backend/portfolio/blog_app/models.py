from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(help_text="article-title", unique=True)
    image = models.ImageField(upload_to="blog/images/")
    content = HTMLField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail_api", kwargs={"slug": self.slug})
