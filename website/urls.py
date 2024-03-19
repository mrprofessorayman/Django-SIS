from django.urls import path
from . import views

urlpatterns = [
    path('<str:guestname>', views.home, name="home"),
]
