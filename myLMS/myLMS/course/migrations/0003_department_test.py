# Generated by Django 4.2 on 2023-04-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_department_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='test',
            field=models.CharField(default='default', max_length=20),
        ),
    ]