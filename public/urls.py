
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import index

urlpatterns = [
    url(r'^$', index, name="index"),
]
