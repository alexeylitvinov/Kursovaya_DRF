from rest_framework import request
from rest_framework.exceptions import ValidationError

from habits.models import Habit


class ValidateActionTime:
    """Валидация времени действия"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value is None:
            return
        field_value = value.get(self.field)
        if field_value is None:
            return
        if field_value > 120:
            raise ValidationError('Время действия должно быть меньше 120 секунд')


class ValidatePeriodicity:
    """Валидация периодичности"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value is None:
            return
        field_value = value.get(self.field)
        if field_value is None:
            return
        if not 1 <= field_value <= 7:
            raise ValidationError('Периодичность не должна быть больше 7 дней')


class ValidateAssociatedHabitOrReward:
    """Валидация связанной привычки или награды"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if value.get(self.field1) and value.get(self.field2):
            raise ValidationError('Должна быть выбрана или связанная привычка или награда')


class ValidateAssociatedHabit:
    """Валидация связанной привычки"""

    def __call__(self, value):
        if value.get('associated_habit') is None:
            return
        associated_habit = (value.get('associated_habit')).id
        if associated_habit:
            if Habit.objects.filter(id=associated_habit, pleasant_habit=True).exists() is False:
                raise ValidationError('В связанную привычку должна быть добавлена только приятная привычка')


class ValidatePleasantHabit:
    """Валидация приятной привычки"""

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        if value.get(self.field1) and (value.get(self.field2) is not None or value.get(self.field3) is not None):
            raise ValidationError('У приятной привычки не может быть связанной привычки или награды')
