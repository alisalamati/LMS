# Generated by Django 4.2 on 2023-04-13 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_department_will_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='will_delete',
        ),
    ]
