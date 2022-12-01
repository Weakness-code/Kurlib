from django.db import models


class Documents(models.Model):
    title = models.CharField("Название документа", max_length=250)
    file = models.FileField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = 'Документы'

class Reports(models.Model):

    title = models.CharField("Название отчета", max_length=250)
    file = models.FileField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = 'Отчеты'