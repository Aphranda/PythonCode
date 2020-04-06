from django.contrib import admin
from django.urls import path, re_path

from clog import views

urlpatterns = [
    re_path("index/", views.index, name="index")
]