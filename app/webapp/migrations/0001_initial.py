# Generated by Django 4.1.7 on 2023-02-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя Автора')),
                ('email', models.EmailField(max_length=500, verbose_name='Почта')),
                ('text', models.TextField(max_length=10000, verbose_name='Текст записи')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('edit_time', models.DateTimeField(null=True, verbose_name='Время редактирования')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=200, verbose_name='Статус')),
            ],
        ),
    ]