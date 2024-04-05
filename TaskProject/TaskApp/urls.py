from django.urls import path
from .views import (home, TaskManagerAPI)

urlpatterns = [
    path(r"", home, name="home"),
    path('persons/',TaskManagerAPI.as_view()),
]