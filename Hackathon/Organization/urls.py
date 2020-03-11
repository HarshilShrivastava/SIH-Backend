from django.contrib import admin
from django.urls import path, include
from .views import Companyprofile,jobviewset,RecommendedJobviewset,applyforjob,get_job
from rest_framework import routers
router = routers.DefaultRouter()
router.register("get-job",jobviewset, basename='jobModel')
router.register("get-recomendedjob",RecommendedJobviewset, basename='recomendedjobModel')

urlpatterns = [
path('create/',Companyprofile.as_view(),name="create C"),
#path('create-job/',Jobsprofile.as_view(),name="create job"),
#path('add/',add_application,name="apply job"),
path("api/", include(router.urls)),
path('add-job/<int:id>/',applyforjob),
path('get-job/<int:id>/',get_job),

]

