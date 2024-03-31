from django.db import models

# Create your models here.


class Social(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = verbose_name + "s"


class SocialItem(models.Model):
    social = models.ForeignKey(Social, on_delete=models.CASCADE, related_name="socials")
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Social Item"
        verbose_name_plural = verbose_name + "s"
