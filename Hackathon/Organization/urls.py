from django.contrib import admin
from django.urls import path, include
from .views import Companyprofile,jobviewset,AllJobViews,list_of_application,Recommendedjobs
from rest_framework import routers
router = routers.DefaultRouter()
router.register("get-job",jobviewset, basename='jobModel')

urlpatterns = [
path('create/',Companyprofile.as_view(),name="create C"),
path("api/", include(router.urls)),
path('get-jobs',Recommendedjobs,name="recommended jobs"),
path('list-of-job/',AllJobViews.as_view()),
path('application-list/<int:id>',list_of_application)

]

