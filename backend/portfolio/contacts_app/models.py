from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    date_recive = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.email


class Phone(models.Model):
    contact = models.ForeignKey(
        ContactInfo, on_delete=models.CASCADE, related_name="phones"
    )
    phone_number = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.phone_number


