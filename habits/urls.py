from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (HabitsListAPIView, HabitsCreateAPIView, HabitsPublishedListAPIView, HabitsRetrieveAPIView,
                          HabitsUpdateAPIView, HabitsDestroyAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitsListAPIView.as_view(), name="habits_list"),
    path("habits_published/", HabitsPublishedListAPIView.as_view(), name="habits_published",),
    path("create/", HabitsCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", HabitsRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("<int:pk>/update/", HabitsUpdateAPIView.as_view(), name="habit_update"),
    path("<int:pk>/delete/", HabitsDestroyAPIView.as_view(), name="habit_delete"),
]
