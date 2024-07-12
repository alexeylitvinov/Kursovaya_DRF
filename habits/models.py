from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """
    Модель привычки
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    place = models.CharField(max_length=255, **NULLABLE, verbose_name='Место')
    time = models.TimeField(**NULLABLE, verbose_name='Время')
    action = models.CharField(max_length=255, verbose_name='Действие')
    pleasant_habit = models.BooleanField(default=False, verbose_name='Приятная привычка')
    associated_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Связанная привычка'
    )
    periodicity = models.PositiveSmallIntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='Награда')
    action_time = models.PositiveSmallIntegerField(default=120, verbose_name='Время действия (ceк)')
    is_public = models.BooleanField(default=False, verbose_name='Публичная привычка')

    class Meta:
        db_table = 'habits'
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'Я буду в {self.action} в {self.time} в {self.place}'
