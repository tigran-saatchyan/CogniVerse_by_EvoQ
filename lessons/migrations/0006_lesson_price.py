# Generated by Django 4.2.5 on 2023-09-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_lesson_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
