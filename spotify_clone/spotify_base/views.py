from django.shortcuts import render

# Create your views here.

default_context = {
    "title": "Spotify Clone - Ankur Jaiswal"
}


def home_view(request):
    return render(request, template_name="base.html", context=default_context)
