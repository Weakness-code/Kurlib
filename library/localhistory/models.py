from django.db import models


class LocalHistoryModel(models.Model):
    title = models.CharField("Оглавление", max_length=250)
    description = models.TextField("Содержание")
    images = [models.ImageField("Изображение", upload_to="localhistory/") for i in range(10)]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Краеведческая статья"
        verbose_name_plural = "Краеведческие статьи"