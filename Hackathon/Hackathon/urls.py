"""Hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from customquiz.api.v0.views import import_question,import_answer,QuestiontListViewset

from rest_framework import routers
router = routers.DefaultRouter()
router.register("get-question",QuestiontListViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("quiz.api.urls")),
    path('account/',include("User.api.urls")),
    path("candidate/",include("Candidate.urls")),
    path("organization/",include("Organization.urls")),
    #path('customquiz/',include("customquiz.api.v0.urls")),
    path("content/",include("content.api.v0.urls")),
    path('customquestion/',import_question,name="questions"),
    path('customanswer/',import_answer,name="answers"),
    path("api/", include(router.urls)),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
