# Generated by Django 5.1.2 on 2024-12-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_remove_talkdetail_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='location',
        ),
        migrations.AddField(
            model_name='conference',
            name='note',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
    ]
