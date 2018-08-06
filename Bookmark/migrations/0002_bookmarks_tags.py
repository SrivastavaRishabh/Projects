# Generated by Django 2.1 on 2018-08-06 09:09

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('Bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarks',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
