from django.db import models
from users.models import User


class Habit(models.Model):
    """Модель привычки"""

    owner = models.ForeignKey(
        User,
        related_name="habits",
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        blank=True,
        null=True,
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место выполнения привычки",
        blank=True,
        null=True,
    )
    time = models.TimeField(
        verbose_name="Время начала выполнения привычки",
        help_text="Выберете дату и время начала привычки",
        blank=True,
        null=True,
    )
    action = models.CharField(
        max_length=255, verbose_name="Действие привычки", help_text="Опишите привычку"
    )
    is_habit_nice = models.BooleanField(
        default=False,
        verbose_name="Признак прятной привычки",
        help_text="Приятная ли привычка",
    )
    is_related = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связання привычка",
        help_text="Выберите связанную привычку",
        null=True,
        blank=True,
    )
    periodicity = models.SmallIntegerField(
        default=1, verbose_name="Периодичность (в днях) - от 1 до 7"
    )
    prize = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
        help_text="Опишите вознаграждение",
    )
    duration = models.SmallIntegerField(
        verbose_name="Время на выполнение прывычки",
        help_text="Укажите время на выполнение привычки в секундах",
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Признак публичности",
        help_text="Опубликовать привычку",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
