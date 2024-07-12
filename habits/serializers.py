from rest_framework import serializers

from habits.models import Habit
from habits.validators import ValidateActionTime, ValidatePeriodicity, ValidateAssociatedHabit, \
    ValidateAssociatedHabitOrReward, ValidatePleasantHabit


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели привычка
    """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            ValidateActionTime(field='action_time'),
            ValidatePeriodicity(field='periodicity'),
            ValidateAssociatedHabitOrReward(field1='associated_habit', field2='reward'),
            ValidateAssociatedHabit(),
            ValidatePleasantHabit(field1='pleasant_habit', field2='associated_habit', field3='reward')
        ]
