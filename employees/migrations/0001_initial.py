# Generated by Django 4.2 on 2023-04-10 03:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Должность')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активна?')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='ФИО')),
                ('contacts', models.CharField(max_length=200, verbose_name='Контакты')),
                ('start_date', models.DateField(default=datetime.date(2023, 4, 10), verbose_name='Дата начала работы')),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Оклад')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='employees.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
