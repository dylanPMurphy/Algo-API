from django.urls import path
from . import views, api
urlpatterns = [
    path('', views.index),
    path('isValidIP/', api.isValidIP)
]