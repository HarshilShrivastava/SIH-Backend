from django.contrib import admin
from django.urls import path, include
from .views import (
    profile,
    applyforjob,
    list_of_job,
    put_ratingM,
    put_ratingT,
    put_generalmarks,
    put_domainmarks,
    put_sub_domainmarks,
    Fullmarks
)

urlpatterns = [
    path('create/',profile.as_view(),name="create C"),
    path('apply/<int:id>/',applyforjob,name="application"),
    path('get-application/',list_of_job,name="list of applied job"),
    path('put-ratingM/',put_ratingM,name="put market rating"),
    path('put-ratingT/',put_ratingT,name="put market rating"),
    path('put-general-marks/',put_generalmarks,name="put general marks"),
    path('put-domain-marks/',put_domainmarks,name="put domain marks"),
    path('put-sub-domain-marks/',put_sub_domainmarks,name="put sub domain marks"),
    path('Fullmarks/',Fullmarks.as_view(),name="get or post full marks")
]

