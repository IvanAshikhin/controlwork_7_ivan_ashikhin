from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import GuestBook


def index_view(request: WSGIRequest):
    guestbook = GuestBook.objects.exclude(status='blocked').order_by('-create_time')
    return render(request, 'index.html', context={'guestbook': guestbook})
