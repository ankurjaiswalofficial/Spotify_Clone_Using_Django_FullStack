# Generated by Django 4.2.1 on 2023-06-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_base', '0005_alter_spotifysongmodel_song_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spotifysongmodel',
            name='song_name',
        ),
        migrations.AlterField(
            model_name='spotifysongmodel',
            name='song_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='spotify_song_category', to='spotify_base.songcategorymodel'),
        ),
    ]
