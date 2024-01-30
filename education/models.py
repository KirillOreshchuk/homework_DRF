from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Курс')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='education/', **NULLABLE, verbose_name='Фото')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name',]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Урок')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='education/', **NULLABLE, verbose_name='Фото')
    video_url = models.CharField(max_length=200, **NULLABLE, verbose_name='Ссылка на видео')

    course = models.ForeignKey('education.Course', on_delete=models.SET_NULL, null=True,
                               verbose_name='Курс', related_name='lessons')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Урок'
        ordering = ['name', ]

    def __str__(self):
        return self.name


    