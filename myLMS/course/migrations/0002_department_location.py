# Generated by Django 4.2 on 2023-04-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.CharField(default='default', max_length=20),
        ),
    ]
