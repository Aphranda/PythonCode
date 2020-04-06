from django.contrib import admin
from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('tables/', views.tables)
]