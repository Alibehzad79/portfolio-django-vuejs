from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100)
    site_about = models.TextField()
    site_logo = models.ImageField(upload_to="site_settings/image/")

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.site_name
