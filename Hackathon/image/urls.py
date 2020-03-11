from django.urls import path, include
from .views import QuestiontListViewset

from rest_framework import routers
router = routers.DefaultRouter()
router.register("get",QuestiontListViewset)

urlpatterns = [
path("api/", include(router.urls)),

]