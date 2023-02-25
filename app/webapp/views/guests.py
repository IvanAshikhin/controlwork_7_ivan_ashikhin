from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import GuestForm
from webapp.models import GuestBook


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = GuestForm()
        return render(request, 'guests_add.html', context={'form': form})
    form = GuestForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'guests_add.html', context={'form': form})
    else:
        GuestBook.objects.create(**form.cleaned_data)
        return redirect('index_page')


def delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_confitm_delete.html', context={"article": article})