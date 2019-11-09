from django.urls import path, include

from minhaapp import views

urlpatterns = [
    path('', views.index),
]