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
    guest = get_object_or_404(GuestBook, pk=pk)
    return render(request, 'confirm_delete.html', context={"guest": guest})


def confirm_delete(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    guest.delete()
    return redirect('index_page')


def update_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == "POST":
        guest.name = request.POST.get('name')
        guest.email = request.POST.get('email')
        guest.text = re
        guest.save()
        return redirect('detail_task', pk=guest.pk)
    return render(requset, 'update.html', context={'guest': guest})
