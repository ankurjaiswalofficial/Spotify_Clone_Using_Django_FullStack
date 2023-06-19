from django.shortcuts import render
from .models import *

# Create your views here.

default_context = {
    "title": "Spotify Clone - Ankur Jaiswal"
}


def home_view(request):
    playlist_model = SpotifyPlayListModel.objects.all()
    song_model = SpotifySongModel.objects.all()
    default_context["playlist_model"] = playlist_model
    default_context["song_model"] = song_model
    return render(request, template_name="base.html", context=default_context)
