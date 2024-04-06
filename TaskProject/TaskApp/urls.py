from django.urls import path
from .views import (home, TaskManagerAPI)

urlpatterns = [
    path(r"", home, name="home"),
    path('task/',TaskManagerAPI.as_view()),
]