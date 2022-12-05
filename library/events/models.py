from django.db import models

def month_determination(month: int):
    months = {1: "Января",
             2: "Февраля",
             3: "Марта",
             4: "Апреля",
             5: "Мая",
             6: "Июня",
             7: "Июля",
             8: "Августа",
             9: "Сентября",
             10: "Октября",
             11: "Ноября",
             12: "Декабря",
             }
    return months[month]
class Event(models.Model):
    title = models.CharField('Наименование мероприятия', max_length=250)
    main_info = models.TextField("Информация по мероприятию")
    date = models.DateField('Дата проведения')
    month = ""
    images = {f'image_{i}': models.ImageField(f'Изображение_1', upload_to="events/", default=None) for i in range(10)}

    def save(self, *args, **kwargs):
        self.month = month_determination(self.date.month)

        super(Event, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"