# Generated by Django 2.1 on 2018-08-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0002_remove_person_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default='rishabh'),
            preserve_default=False,
        ),
    ]
