from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

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
    guest = get_object_or_404(GuestBook, pk=pk)
    return render(request, 'confirm_delete.html', context={"guest": guest})


def confirm_delete(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    guest.delete()
    return redirect('index_page')


def update_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = GuestForm(instance=guest)
        return render(request, 'update.html', {'form': form, 'guest': guest})
    elif request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.edit_time = datetime.now()
            guest.save()
            return redirect('index_page')
        else:
            return render(request, 'update.html', {'form': form, 'guest': guest})
