from django.db import models

class Rules(models.Model):
    rule = models.TextField("Правило")

    def __str__(self):
        return self.rule

    class Meta:
        verbose_name = "Правило"
        verbose_name_plural = 'Правила'


class NewWork(models.Model):
    title = models.CharField("Название работы", max_length=250)
    cover = models.ImageField("Обложка работы", upload_to="works/")
    description = models.TextField("Описание работы")
    author = models.CharField("Автор работы", max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"


class VirtualCard(models.Model):
    title = models.CharField("Название книги", max_length=250)
    cover = models.ImageField("Обложка", upload_to='books/')
    anons = models.TextField("Приписка")
    description = models.TextField("Описание книги")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Competition(models.Model):
    title = models.CharField("Название конкурса", max_length=250)
    image = models.ImageField("Изображение для конкурса", upload_to="competition/")
    description = models.TextField("Информация по конкурсу")
    date_begin = models.DateField("Дата начала конкурса")
    date_end = models.DateField("Дата конца конкурса")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Конкурс"
        verbose_name_plural = "Конкурсы"