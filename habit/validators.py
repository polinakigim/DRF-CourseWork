from rest_framework.exceptions import ValidationError


class PeriodicityValidator:
    """Периодичность должна быть от 1 до 7 дней"""

    def __call__(self, value):
        periodicity = value.get("periodicity")
        if periodicity is not None and not (1 <= periodicity <= 7):
            raise ValidationError("Периодичность должна быть от 1 до 7 дней.")



class DurationValidator:
    """Время выполнения должно быть не больше 120 секунд"""

    def __call__(self, value):
        if value.get("duration") and value["duration"] > 120:
            raise ValidationError(
                "Время выполнения привычки не должно превышать 120 секунд."
            )


class RelatedHabitMustBePleasantValidator:
    """В связанные привычки могут попадать только приятные привычки"""

    def __call__(self, value):
        related = value.get("is_related")
        if related and not related.is_habit_nice:
            raise ValidationError("Связанная привычка должна быть приятной.")


class PleasantHabitValidator:
    """Приятная привычка не может иметь prize или is_related"""

    def __call__(self, value):
        if value.get("is_habit_nice"):
            if value.get("prize") or value.get("is_related"):
                raise ValidationError(
                    "Приятная привычка не может иметь вознаграждение или связанную привычку."
                )


from rest_framework.exceptions import ValidationError


class PrizeAndRelatedValidator:
    """Нельзя одновременно указывать и prize, и is_related"""

    def __call__(self, value):
        if value.get("prize") and value.get("is_related"):
            raise ValidationError(
                "Нельзя одновременно указывать и вознаграждение, и связанную привычку."
            )
