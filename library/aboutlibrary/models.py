from django.db import models


class Documents(models.Model):
    title = models.CharField("Название документа", max_length=250)
    file = models.FileField("Документ.pdf", upload_to='documents/')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = 'Документы'

class Reports(models.Model):

    title = models.CharField("Название отчета", max_length=250)
    file = models.FileField("Отчет.pdf", upload_to='reports/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = 'Отчеты'


class Cites(models.Model):

    title = models.CharField("Название сайта", max_length=250)
    address = models.URLField("Ссылка на сайт")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сайт Курагинсого района"
        verbose_name_plural = 'Сайты Курагинсого района'