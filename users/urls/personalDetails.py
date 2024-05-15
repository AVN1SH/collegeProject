from django.contrib import admin
from django.urls import path
from users.views.personalDetails import Personal_Details_View
from users.models.personalDetails import Personal_Details

urlpatterns = [
    path("personalDetails/",Personal_Details_View.as_view()),
    path("updatePersonalDetails/<int:pk>",Personal_Details_View.as_view()),
    path("getPersonalDetails/",Personal_Details_View.as_view()),
    path("getPersonalDetails/<int:pk>",Personal_Details_View.as_view()),
    path("deletepersonalDetails/<int:pk>",Personal_Details_View.as_view()),
]