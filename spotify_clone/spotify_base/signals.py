from django.db.models.signals import post_save
from django.dispatch import receiver
import eyed3
import uuid
from .models import SpotifySongModel


@receiver(post_save, sender=SpotifySongModel)
def data_updater(sender, instance, **kwargs):
    if len(str(instance.song_thumbnail)) == 0:
        audio_file = eyed3.load("media/" + str(instance.song_file))
        album_name = audio_file.tag.album
        artist_name = audio_file.tag.artist
        location = "media/" + str(instance.song_file).removesuffix(str(instance.song_file).split("/")[-1])
        filename = "{0}_.jpg".format(uuid.uuid4())
        instance.song_artist = artist_name
        instance.song_album = album_name
        instance.song_description = "Song for you by \"{0}\" from the Album \"{1}\"".format(artist_name, album_name)
        for image in audio_file.tag.images:
            image_file = open(location + "/" + filename, "wb")
            image_file.write(image.image_data)
            image_file.close()
        instance.song_thumbnail = str(instance.song_file).removesuffix(
            str(instance.song_file).split("/")[-1]) + filename
        print(album_name,
              artist_name,
              instance.song_album,
              instance.song_artist,
              filename,
              instance.song_description,
              instance.song_thumbnail)
        instance.save()
