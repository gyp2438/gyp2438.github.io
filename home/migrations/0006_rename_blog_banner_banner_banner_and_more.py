# Generated by Django 5.1.2 on 2024-10-30 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_meme_me'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='blog_banner',
            new_name='banner',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='home_banner',
        ),
    ]
