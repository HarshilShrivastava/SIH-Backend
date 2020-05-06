from django.contrib import admin
from django.urls import path, include
from .views import (
    profile,
    applyforjob,
    list_of_job,
    put_ratingM,
    put_ratingT
)

urlpatterns = [
    path('create/',profile.as_view(),name="create C"),
    path('apply/<int:id>/',applyforjob,name="application"),
    path('get-application/',list_of_job,name="list of applied job"),
    path('put-ratingM/',put_ratingM,name="put market rating"),
    path('put-ratingT/',put_ratingT,name="put market rating"),
]

