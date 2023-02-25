from django.contrib import admin

from webapp.models import GuestBook


# Register your models here.


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'text', 'create_time', 'edit_time', 'status')
    list_filter = ('id', 'name', 'email', 'text', 'create_time', 'edit_time', 'status')
    search_fields = ('id', 'name', 'email', 'status')
    fields = ('id', 'name', 'email', 'text', 'create_time', 'edit_time', 'status')
    readonly_fields = ('id', 'create_time', 'edit_time')


admin.site.register(GuestBook, GuestBookAdmin)