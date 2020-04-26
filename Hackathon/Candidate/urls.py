from django.contrib import admin
from django.urls import path, include
from .views import profile,applyforjob,list_of_job
urlpatterns = [
path('create/',profile.as_view(),name="create C"),
path('apply/<int:id>/',applyforjob,name="application"),
path('get-application/',list_of_job,name="list of applied job")

]

