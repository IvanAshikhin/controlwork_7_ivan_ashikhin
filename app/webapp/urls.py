from django.urls import path

from webapp.views import guests
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name="index_page"),
    path('guest/add/', guests.add_view, name="add_guest"),
    path('guest/<int:pk>/delete', guests.delete_view, name='delete_guest'),
    path('guest/<int:pk>/confirm_delete', guests.confirm_delete, name='confirm_delete'),
    path('guest/<int:pk>/update', guests.update_view, name='guest_update')
]
