# Generated by Django 4.2.6 on 2023-10-24 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_client_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_create',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
