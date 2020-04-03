from django.urls import path
from University.views import Companyprofile,applyforjobUniversity

urlpatterns = [
path("Uprofile/",Companyprofile.as_view(),name="profile"),
path("apply/<int:id>/",applyforjobUniversity,name="apply")

    
 ]
