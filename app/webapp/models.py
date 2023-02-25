from django.db import models

# Create your models here.

STATUS = (('active', 'Активно'), ('blocked', 'Заблокировано'))


class GuestBook(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя Автора')
    email = models.EmailField(max_length=500, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=10000, null=False, blank=False, verbose_name='Текст записи')
    create_time = models.DateTimeField(auto_now=True, null=False, verbose_name='Время создания')
    edit_time = models.DateTimeField(auto_now=False, null=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=200, verbose_name='Статус', choices=STATUS, default='active')

    def __str__(self):
        return f'{self.name} - {self.email} - {self.text} - {self.create_time} - {self.edit_time} - {self.status}'
