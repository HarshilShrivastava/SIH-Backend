from django.shortcuts import render
from .models import Recruit,Skill,MCQresult
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Recruit
from rest_framework.authentication import TokenAuthentication

from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import RecruitSerializer
from rest_framework.views import APIView


class profile(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}

        if request.user.Is_Candidate == 1:
            serializer = RecruitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                context['sucess']=True
                context['status']=200
                data=serializer.data
                context['data']=data
                return Response(context)
            else:
                context['sucess']=False
                context['status']=400
                data=serializer.errors
                context['data']=data
                return Response(context)

    def get(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.Is_Candidate == 1:
            try:
                obj=get_object_or_404(Recruit,User=request.user)
            except:
                context['sucess']=False
                context['status']=400
                context['data']=data
                return Response(context)
            serializer = RecruitSerializer(obj)
            context['sucess']=True
            context['status']=200
            data=serializer.data
            context['data']=data
            return Response(context)

            
    def put(self, request, *args, **kwargs):
        if request.user.Is_Candidate == 1:
            obj=get_object_or_404(Recruit,User=request.user)
            serializer = RecruitSerializer(obj,data=request.data)
            context={}
            data={}
            if serializer.is_valid():
                serializer.save()
                context['sucess']=True
                context['status']=200
                data=serializer.data
                context['data']=data
                return Response(context)
            context['sucess']=False
            context['status']=400
            data=serializer.errors
            context['data']=data
            return Response(context)
            
