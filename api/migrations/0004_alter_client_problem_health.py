# Generated by Django 4.2.6 on 2023-10-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_client_problem_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='problem_health',
            field=models.ManyToManyField(related_name='problem', to='api.problemshealth'),
        ),
    ]