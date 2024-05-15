from django.contrib import admin
from django.urls import path
from users.views.qualification import Qualification_View

urlpatterns = [
    path("qualification/",Qualification_View.as_view()),
    path("updateQualification/<int:pk>",Qualification_View.as_view()),
    path("getQualification/",Qualification_View.as_view()),
    path("getQualification/<int:pk>",Qualification_View.as_view()),
    path("deleteQualification/<int:pk>",Qualification_View.as_view()),
]