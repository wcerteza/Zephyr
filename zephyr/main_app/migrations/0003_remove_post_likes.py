# Generated by Django 4.2.2 on 2023-06-19 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
