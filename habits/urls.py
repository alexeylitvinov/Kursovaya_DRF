from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDetailAPIView, \
    HabitDeleteAPIView, HabitPublicListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habits'),
    path('public/', HabitPublicListAPIView.as_view(), name='public_habits'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('habits/<int:pk>/', HabitDetailAPIView.as_view(), name='detail_habit'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('habits/<int:pk>/delete/', HabitDeleteAPIView.as_view(), name='delete_habit'),
]
