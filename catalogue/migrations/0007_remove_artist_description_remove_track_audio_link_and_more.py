# Generated by Django 4.2.7 on 2023-12-04 02:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_rename_title_album_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='description',
        ),
        migrations.RemoveField(
            model_name='track',
            name='audio_link',
        ),
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='bio',
            field=models.TextField(default='the artist is you'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='release_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.artist'),
            preserve_default=False,
        ),
    ]