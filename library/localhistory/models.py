from django.db import models


class LocalHistoryModel(models.Model):

    CHAPTERS = [
        (1, 'Курагинский район'),
        (2, 'Курагино'),
        (3, 'Села и поселки'),
        (4, 'Мемориальные доски'),
        (5, 'Курагинцы в годы ВОВ'),
        (6, 'Литературная карта'),
        (7, 'Культура. Искусство. Библиотечное дело'),
        (8, 'Имя в истории района')
    ]

    title = models.CharField("Оглавление", max_length=250)
    chapter = models.PositiveSmallIntegerField('Раздел', choices=CHAPTERS, blank=False)
    description = models.TextField("Содержание")
    edited_description = ''

    image_0 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_1 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_2 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_3 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_4 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_5 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_6 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_7 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_8 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_9 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_10 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_11 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_12 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_13 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_14 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_15 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_16 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_17 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_18 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)
    image_19 = models.ImageField("Изображение", upload_to=f"localhistory/", blank=True)

    images = list()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Краеведческая статья"
        verbose_name_plural = "Краеведческие статьи"