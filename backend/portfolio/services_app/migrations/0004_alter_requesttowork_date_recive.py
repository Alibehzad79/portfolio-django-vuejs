# Generated by Django 5.0.3 on 2024-03-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0003_alter_serviceoption_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttowork',
            name='date_recive',
            field=models.DateField(),
        ),
    ]
