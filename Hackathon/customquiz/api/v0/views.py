from customquiz.models import(
     Answer,
     
     Question,
     SubDomain,
     )
import csv
import urllib
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from customquiz.api.v0.serializers import (
     questionSerializer,
     AnswerSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Organization.models import(
     Company
)


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
          return Response("Hellosb")
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


