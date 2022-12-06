from django.db import models

class Billboard(models.Model):
    title = models.CharField("Заголовок", max_length=250)
    text = models.TextField('Содержание(Не обязательно)', blank=True)
    image = models.ImageField("Изображение", upload_to='Billboard/')
    hidden = models.BooleanField("Скрыть пост", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мини-пост для афиши"
        verbose_name_plural = "Мини-посты для афиши"

class QuestionAnswer(models.Model):
    question = models.TextField("Часто задаваемый вопрос")
    answer = models.TextField("Ответ")
    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Часто задаваемые вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"

class Partners(models.Model):
    icon = models.ImageField("Иконка", upload_to='partners_ico/')
    title = models.CharField("Наименование", max_length=250)
    url = models.URLField("Страница партнера(Не обязательно)", blank=True)
    number = int()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"