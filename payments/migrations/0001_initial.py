# Generated by Django 5.0.1 on 2024-01-21 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0002_lesson_course'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='Дата оплаты')),
                ('payment_amount', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'Перевод')], default='card', max_length=10, verbose_name='Способ оплаты')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.course', verbose_name='Курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.lesson', verbose_name='Урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
                'ordering': ['-payment_date'],
            },
        ),
    ]