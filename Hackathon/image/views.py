from django.shortcuts import render

# Create your views here.fr
from .models import image
from rest_framework.decorators import (
    permission_classes,
)
from .serializers import AnswerSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from rest_framework.response import Response

class QuestiontListViewset(viewsets.ModelViewSet):
    queryset = image.objects.all()
    permission_classes=[AllowAny]
    serializer_class = AnswerSerializer
    http_method_names = ['get','POST']


    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'Question_list': serializer.data})