from rest_framework import generics

from habit.models import Habit
from habit.paginators import CustomPagination
from habit.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    """Лист отображающий привычки конкретного пользователя."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)
    pagination_class = CustomPagination


class HabitPublicListAPIView(generics.ListAPIView):
    """Лист отображающий публичные привычки пользователей."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Habit.objects.filter(is_public=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Детали привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Обновление привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)
