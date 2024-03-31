from django.db import models

# Create your models here.


class Resume(models.Model):
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return "Resume"


class Education(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="educations"
    )
    title = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.title


class Experiance(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="experiances"
    )
    title = models.CharField(max_length=100)
    at = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Experiance"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.title


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.title
