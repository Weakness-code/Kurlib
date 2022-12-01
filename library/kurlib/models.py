from django.db import models


class Branches(models.Model):
    title = models.CharField("Название филиала", max_length=250)
    weekend = models.CharField("Выходные дни", max_length=250)
    manager = models.CharField("Заведующая", max_length=250)
    lunch_break = models.CharField("Перерыв на обед", max_length=250)
    working_hours = models.CharField("Время работы", max_length=250)

    def __str__(self):
        return self.title

