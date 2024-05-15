from django.contrib import admin
from django.urls import path
from users.views.document import Document_View
from users.views.all_data import All_Data_View

urlpatterns = [
    path("document/",Document_View.as_view()),
    path("updateDocument/<int:pk>",Document_View.as_view()),
    path("getDocument/",Document_View.as_view()),
    path("getDocument/<int:pk>",Document_View.as_view()),
    path("deleteDocument/<int:pk>",Document_View.as_view()),
    path("getAllData/<int:pk>",All_Data_View.as_view()),

]