# Generated by Django 5.1.2 on 2024-10-31 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('page', models.SlugField(blank=True, help_text="Enter the template name, e.g., 'home', 'about'", unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('email', models.CharField(blank=True, max_length=60)),
                ('affiliation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='person', to='home.location')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(help_text='Markdown text enabled')),
                ('github', models.URLField(blank=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('person', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.person')),
            ],
            options={
                'verbose_name_plural': 'Me',
            },
        ),
    ]
