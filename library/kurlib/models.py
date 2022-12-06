from django.db import models

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
    number = int()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"