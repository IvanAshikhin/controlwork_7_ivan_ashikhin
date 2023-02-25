from django.urls import path

from webapp.views import guests
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name="index_page"),
    path('article/add/', guests.add_view, name="add_guest"),
]
