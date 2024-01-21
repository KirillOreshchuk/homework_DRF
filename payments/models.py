from django.db import models

from config import settings
from education.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}

METHOD_CHOICES = [
    ('cash', 'Наличные'),
    ('transfer', 'Перевод'),
]


class Payment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='payments', verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Урок')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=10, choices=METHOD_CHOICES,
                                      default='card', verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ['-payment_date',]

    def __str__(self):
        return f'{self.user}: {self.payment_amount} {self.payment_date}'
