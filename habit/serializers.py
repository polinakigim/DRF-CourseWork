from rest_framework import serializers

from habit.models import Habit
from habit.validators import (DurationValidator, PeriodicityValidator,
                              PleasantHabitValidator, PrizeAndRelatedValidator,
                              RelatedHabitMustBePleasantValidator)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            PrizeAndRelatedValidator(),
            PleasantHabitValidator(),
            RelatedHabitMustBePleasantValidator(),
            DurationValidator(),
            PeriodicityValidator(),
        ]
