from django.db import models

# Create your models here.


class MyProfile(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    whate_am_i = models.CharField(max_length=100, blank=True, null=True)
    my_description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="profile/imgs/", blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.full_name
