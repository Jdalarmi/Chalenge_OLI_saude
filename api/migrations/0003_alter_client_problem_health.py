# Generated by Django 4.2.6 on 2023-10-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_client_problem_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='problem_health',
            field=models.ManyToManyField(blank=True, related_name='problem', to='api.problemshealth'),
        ),
    ]
