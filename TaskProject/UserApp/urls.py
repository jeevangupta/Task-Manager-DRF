from django.urls import path
from .views import (register_view, login_view, logout_view, test_token)

urlpatterns = [
    path('register/',register_view),
    path('login/',login_view),
    path('logout/',logout_view),
    path('test-token/',test_token),
    
]