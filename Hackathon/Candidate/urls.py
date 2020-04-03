from django.contrib import admin
from django.urls import path, include
from .views import profile,applyforjob
urlpatterns = [
path('create/',profile.as_view(),name="create C"),
path('apply/<int:id>/',applyforjob,name="application"),

]

