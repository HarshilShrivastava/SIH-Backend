from django.urls import path, include
from .views import QuestiontListViewset,DomainQuestiontListViewset,putgeneralmarks,putdomainmarks

from rest_framework import routers
router = routers.DefaultRouter()
router.register("get-question",QuestiontListViewset)
router.register("get-domain-question",DomainQuestiontListViewset)

urlpatterns = [
path("api/", include(router.urls)),
path("put-general-marks/",putgeneralmarks,name="put general marks"),
path("put-domain-marks/",putdomainmarks,name="put general marks")
]