from django.contrib import admin
from django.urls import path, include
from .views import Companyprofile,jobviewset,RecommendedJobviewset,AllJobViews,list_of_application
from rest_framework import routers
router = routers.DefaultRouter()
router.register("get-job",jobviewset, basename='jobModel')
router.register("get-recomendedjob",RecommendedJobviewset, basename='recomendedjobModel')

urlpatterns = [
path('create/',Companyprofile.as_view(),name="create C"),
path("api/", include(router.urls)),
path('list-of-job/',AllJobViews.as_view()),
path('application-list/<int:id>',list_of_application)

]

