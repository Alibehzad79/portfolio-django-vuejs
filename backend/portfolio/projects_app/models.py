from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = HTMLField()
    image = models.ImageField(upload_to="projects/images/")
    client = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    completed_date = models.DateField(auto_now=False, auto_now_add=False)
    website = models.URLField(max_length=200)


class ProjectGallery(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="galleries"
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="projects/images/")

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title
