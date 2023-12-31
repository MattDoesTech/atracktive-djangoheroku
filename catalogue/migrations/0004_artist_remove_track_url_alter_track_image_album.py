# Generated by Django 4.2.7 on 2023-11-29 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_alter_track_audio_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='catalogue/images/artists')),
            ],
        ),
        migrations.RemoveField(
            model_name='track',
            name='url',
        ),
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(upload_to='catalogue/images/tracks'),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='catalogue/images/albums')),
                ('artist', models.ManyToManyField(to='catalogue.artist')),
                ('tracks', models.ManyToManyField(to='catalogue.track')),
            ],
        ),
    ]
