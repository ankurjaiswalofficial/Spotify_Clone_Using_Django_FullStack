# Generated by Django 4.2.1 on 2023-06-10 17:28

from django.db import migrations, models
import django.utils.timezone
import spotify_base.models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotifysongmodel',
            name='song_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to=spotify_base.models.generate_uuid4_filename, verbose_name='Song File'),
            preserve_default=False,
        ),
    ]