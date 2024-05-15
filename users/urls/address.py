from django.contrib import admin
from django.urls import path
from users.models.address import Address_Model
from users.views.address import Address_View

urlpatterns = [
    path("address/",Address_View.as_view()),
    path("getAddress/<int:pk>",Address_View.as_view()),
    path("getAddress/",Address_View.as_view()),
    path("updateAddress/<int:pk>",Address_View.as_view()),
    path("deleteAddress/<int:pk>",Address_View.as_view()),
]