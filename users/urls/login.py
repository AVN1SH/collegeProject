from django.contrib import admin
from django.urls import path
from users.views.login import Login_View
from users.models.registration import User_Model

urlpatterns = [
    path("login/",Login_View.as_view()),
]