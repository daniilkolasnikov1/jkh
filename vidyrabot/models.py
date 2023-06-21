from django.db import models


class Artiles(models.Model):
    title = models.CharField('Фамилия, Имя, Отчество', max_length=100)
    full_text = models.TextField('Текст Обращения')
    summ_uslug = models.TextField('Адрес, номер телефона')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Виды услуг'
        verbose_name_plural = 'Виды услуг'

