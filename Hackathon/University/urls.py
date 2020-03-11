from django.urls import path
from University.views import Companyprofile

urlpatterns = [
path("Uprofile/",Companyprofile.as_view(),name="profile")

    
 ]
