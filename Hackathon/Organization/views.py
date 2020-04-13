from django.shortcuts import render
from .models import Company,Jobs
from rest_framework import filters

from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import companyserializer,jobserializer,jobReadserializer
from rest_framework.views import APIView
from rest_framework import viewsets
from Candidate.models import (
    Recruit
)

from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

class Companyprofile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.Is_Organization == 1:
            serializer = companyserializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                context['sucess']=True
                context['status']=200
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            else:
                context['sucess']=False
                context['status']=400
                context['message']="error"
                data=serializer.errors
                context['data']=data
                return Response(context)
                
        else:
            return Response( status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if request.user.Is_Organization == 1:
            context={}
            data={}
            try:
                obj=get_object_or_404(Company,User=request.user)
            except:
                context['sucess']=False
                context['status']=200
                context['message']="fill the form"
                context['data']=data
                return Response(context)
            
            serializer = companyserializer(obj)
            context['sucess']=True
            context['status']=200
            context['message']="already exist"
            data=serializer.data
            context['data']=data
            return Response(context)
            
    def put(self, request, *args, **kwargs):
        if request.user.Is_Candidate == 1:
            obj=get_object_or_404(Company,User=request.user)
            serializer = companyserializer(obj,data=request.data)
            context={}
            data={}
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                context['sucess']=True
                context['status']=200
                context['message']="sucessfully done"
                data=serializer.data
                context['data']=data
                return Response(context)
            context['sucess']=False
            context['status']=400
            context['message']="not done"
            data=serializer.errors
            context['data']=data
            return Response(context)

 
class jobviewset(viewsets.ModelViewSet):
    serializer_class = jobserializer
    queryset=Jobs.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    http_method_names=['get','post','put','delete']
    def create(self, request,*kwargs):
        context={}
        data={}
        user=self.request.user
        companyobj=Company.objects.get(User=request.user)
        serializer=jobserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(by=companyobj)
            context['sucess']=True
            context['response']="sucessfull"
            context['status']=200
            data=serializer.data
            context['data']=data
            return Response(context)
        else:
            return Response(serializer.errors)


    def list(self, request,*kwargs):
        context={}
        data={}
        user=self.request.user
        companyobj=get_object_or_404(Company,User=user)
        queryset=Jobs.objects.filter(by=companyobj)
        context['sucess']=True
        context['status']=200
        context['response']="sucessfull"
        serializer = jobserializer(queryset,many=True)
        data=serializer.data
        context['data']=data
        return Response(context)
    def post(self,request,*kwargs):
        context={}
        data={}
        user=self.request.user
        companyobj=get_object_or_404(Company,User=user)
        serializer=jobserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(by=companyobj)
            context['sucess']=True
            context['response']="sucessfull"
            context['status']=200
            data=serializer.data
            context['data']=data
            return Response(context)



class RecommendedJobviewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = jobReadserializer
    queryset=Jobs.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Level','fields']

    http_method_names=['get']
    def list(self, request,*kwargs):
        context={}
        data={}
        queryset=Jobs.objects.all()
        context['sucess']=True
        context['status']=200
        context['response']="sucessfull"
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        data=serializer.data
        context['data']=data
        return Response(context)


class AllJobViews(generics.ListCreateAPIView):
    queryset=Jobs.objects.all()
    serializer_class = jobReadserializer
    search_fields = ['^job_title','by__Name']
    filter_backends = (filters.SearchFilter,)
    

