from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.title


class ServiceOption(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service_options"
    )
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Service Option"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.title


class ServicePlan(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service_plans"
    )
    title = models.CharField(max_length=100)
    plan = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = "Service Plan"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.title


class RequestToWork(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="servic_requests"
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_recive = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Service Request"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.name
