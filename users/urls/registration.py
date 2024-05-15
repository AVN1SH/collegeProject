from django.contrib import admin
from django.urls import path
from users.views.registration import User_View
from users.models.registration import User_Model

urlpatterns = [
    path("register/",User_View.as_view()),
    path("updateRegister/<int:pk>",User_View.as_view()),
    path("getRegister/",User_View.as_view()),
    path("getRegister/<int:pk>",User_View.as_view()),
    path("deleteRegister/<int:pk>",User_View.as_view()),
]
