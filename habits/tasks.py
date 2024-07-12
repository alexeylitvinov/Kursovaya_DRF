import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_telegram():
    """
    Отправляет сообщение в телеграм чат за 5 минут до действия привычки
    """
    users = User.objects.filter(tg_chat_id__isnull=False)
    for user in users:
        habits = Habit.objects.filter(user=user, time__isnull=False)
        for habit in habits:
            send_time = datetime.time(
                (habit.time.hour + (habit.time.minute - 5) // 60) % 24,
                (habit.time.minute - 5) % 60
            )
            if send_time.strftime('%H:%M') == datetime.datetime.now().strftime('%H:%M'):
                print('Cообщение отправлено')
                send_telegram_message(user.tg_chat_id, f'{habit.__str__()}')
