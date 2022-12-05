from django.db import models

class QuestionAnswer(models.Model):
    question = models.TextField("Часто задаваемый вопрос")
    answer = models.TextField("Ответ")
    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Часто задаваемые вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"