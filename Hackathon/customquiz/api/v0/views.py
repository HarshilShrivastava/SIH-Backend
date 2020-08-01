from customquiz.models import(
     Answer,
     Question,
     SubDomain,
     )
import csv
import urllib
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

from customquiz.api.v0.serializers import (
     questionSerializer,
     AnswerSerializer,
     AnswerqSerializer,
     QuestionqSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Organization.models import(
     Company
)
from rest_framework import viewsets

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def import_question(request):
     serializer=questionSerializer(data=request.data)
     context={}
     if request.method == "POST":
          if serializer.is_valid():
               user=request.user
               org_obj=get_object_or_404(Company,User=user)
               serializer.save(Organization=org_obj)
               context['sucess']=True
               context['status']=200
               context['message']="sucessfull"
               return Response(context)
          return Response(serializer.errors)
     return Response("Hellob")


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def import_answer(request):
     serializer=AnswerSerializer(data=request.data)
     context={}
     if request.method == "POST":
          if serializer.is_valid():
               user=request.user
               org_obj=get_object_or_404(Company,User=user)
               key=serializer.validated_data['Question_related_to']
               qs=Question.objects.filter(Organization=org_obj)
               obj=qs.get(key=key)
               serializer.save(Question_related_to=obj)
               context['sucess']=True
               context['status']=200
               context['message']="sucessfull"
               return Response(context)
          return Response(serializer.errors)
     return Response("Hellob")


class QuestiontListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionqSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'Question_list': serializer.data})
