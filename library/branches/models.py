from django.db import models


class Branches(models.Model):
    title = models.CharField("Название филиала", max_length=250)
    weekend = models.CharField("Выходные дни", max_length=250)
    manager = models.CharField("Заведующая", max_length=250)
    lunch_break = models.CharField("Перерыв на обед", max_length=250)
    working_hours = models.CharField("Время работы", max_length=250)

    description = models.TextField("Содержание", blank=True, default=None)
    edited_description = ''

    image_0 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_1 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_2 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_3 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_4 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_5 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_6 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_7 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_8 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_9 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_10 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_11 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_12 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_13 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_14 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_15 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_16 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_17 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_18 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)
    image_19 = models.ImageField("Изображение", upload_to=f"Branches/", blank=True)

    images = list()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = 'Филиалы'

