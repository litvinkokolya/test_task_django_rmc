from django.db import models


class TestSet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.title


class Question(models.Model):
    test_set = models.ForeignKey("TestSet", on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        "Question", on_delete=models.CASCADE, related_name="choices"
    )
    text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"

    def __str__(self):
        return self.text


class TestResult(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    test_set = models.ForeignKey("TestSet", on_delete=models.CASCADE)
    result = models.FloatField(verbose_name="Результат (процентов)")

    def __str__(self):
        return f"{self.user}:{self.test_set}:{self.result}%"

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
