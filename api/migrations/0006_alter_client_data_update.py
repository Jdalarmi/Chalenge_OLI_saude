# Generated by Django 4.2.6 on 2023-10-19 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_client_data_update_alter_client_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='data_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]