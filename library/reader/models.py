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
    anons = models.TextField("Вступление")
    author = models.CharField("Автор работы", max_length=250)

    edited_description = ''
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новинка"
        verbose_name_plural = "Книжные новинки"


'''class VirtualCard(models.Model):
    title = models.CharField("Название книги", max_length=250)
    cover = models.ImageField("Обложка", upload_to='books/')
    anons = models.TextField("Вступление")
    description = models.TextField("Описание книги")

    edited_description = ''
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Виртуальная карта"
        verbose_name_plural = "Виртуальная выставка"'''


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