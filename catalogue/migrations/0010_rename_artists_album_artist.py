# Generated by Django 4.2.7 on 2023-12-06 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_track_artist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artists',
            new_name='artist',
        ),
    ]
