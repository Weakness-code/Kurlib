from django.db import models

class Event(models.Model):
    title = models.CharField('Наименование мероприятия', max_length=250)
    main_info = models.TextField("Информация по мероприятию")
    date = models.DateField('Дата проведения')
    image = models.ImageField('Изображение', upload_to="events/")
    month = ''
    edited_info = ''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

