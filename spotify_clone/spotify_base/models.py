from django.db import models
import uuid
import os


def generate_uuid4_filename(instance, filename):
    """
        Generates an uuid4 (random) filename, keeping file extension

        :param filename: Filename passed in. In the general case, this will
                         be provided by django-ckeditor's uploader.
        :return: Randomized filename in urn format.
        :rtype: str
        """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(f'uploads/songs_dir/{uuid.uuid4()}', filename)


# Create your models here.


class SongCategoryModel(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name="Song Category", max_length=50)

    class Meta:
        verbose_name = "SongCategoryModel"
        verbose_name_plural = "SongCategoryModels"

    def __str__(self):
        return self.name


class SpotifySongModel(models.Model):
    objects = models.Manager()
    song_album = models.CharField(verbose_name="Song Album Name", max_length=150, null=True, blank=True)
    song_artist = models.CharField(verbose_name="Song Artist", max_length=150, null=True, blank=True)
    song_description = models.CharField(verbose_name="Song Description", max_length=750, null=True, blank=True)
    song_category = models.ManyToManyField(to=SongCategoryModel, related_name="spotify_song_category",
                                           blank=True)
    song_file = models.FileField(verbose_name="Song File", upload_to=generate_uuid4_filename)
    song_thumbnail = models.ImageField(verbose_name="Song Thumbnail", null=True, blank=True)
    date_time = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        verbose_name = "SpotifySongModel"
        verbose_name_plural = "SpotifySongModels"

    def __str__(self):
        return str(self.song_file)


class SpotifyPlayListModel(models.Model):
    objects = models.Manager()
    playlist_name = models.CharField(verbose_name="PlayList Name", max_length=100)
    playlist_songs = models.ManyToManyField(to=SpotifySongModel, related_name="spotify_playlist_songs")
    playlist_category = models.ManyToManyField(to=SongCategoryModel, related_name="spotify_playlist_category")

    class Meta:
        verbose_name = "SpotifyPlayList"
        verbose_name_plural = "SpotifyPlayLists"

    def __str__(self):
        return self.playlist_name
