from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsUser


class HabitCreateAPIView(CreateAPIView):
    """Создание привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Привязка привычки к пользователю"""
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitPublicListAPIView(ListAPIView):
    """Публичные привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """Получение публичных привычек"""
        return Habit.objects.filter(is_public=True)


class HabitListAPIView(ListAPIView):
    """Список привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = (IsUser,)

    def get_queryset(self):
        """Получение привычек пользователя"""
        return Habit.objects.filter(user=self.request.user)


class HabitDetailAPIView(RetrieveAPIView):
    """Просмотр привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsUser,)


class HabitUpdateAPIView(UpdateAPIView):
    """Редактирование привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsUser,)


class HabitDeleteAPIView(DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsUser,)
