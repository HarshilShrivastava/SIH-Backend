from django.contrib import admin
from django.urls import path, include
from .views import profile
urlpatterns = [
path('create/',profile.as_view(),name="create C"),
]

