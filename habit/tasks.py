from datetime import datetime

import pytz
from celery import shared_task

from config import settings
from habit.models import Habit
from habit.services import send_telegram_message


@shared_task
def send_habit_reminders():
    """
    Проверка привычек и отправка уведомлений.
    """
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone).time()

    habits = Habit.objects.filter(owner__tg_chat_id__isnull=False)

    for habit in habits:
        if habit.time <= now:
            message = f"Напоминание: пора {habit.action}"
            if habit.place:
                message += f" в {habit.place}"

            send_telegram_message(habit.owner.tg_chat_id, message)

            habit.time += habit.get_periodicity_timedelta()
            habit.save()
