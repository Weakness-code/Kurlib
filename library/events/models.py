from django.db import models


class Event(models.Model):
    title = models.CharField('Наименование мероприятия', max_length=250)
    main_info = models.TextField("Информация по мероприятию")
    date = models.DateField('Дата проведения')
    images = {f'image_{i}': models.ImageField(f'Изображение_1', upload_to="events/", default=None) for i in range(10)}

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"