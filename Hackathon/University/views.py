from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Profile,Jobenquiry
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required 
from Organization.models import Jobs
from rest_framework.response import Response
from .serializers import UniversitySerializer,JobenquirySerializer
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
# Create your views here.
class Companyprofile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    def post(self, request, *args, **kwargs):

        context={}
        data={}
        if request.user.Is_University == 1:
            serializer = UniversitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            else:
                context['status']=400
                context['sucess']=False
                context['message']="not  created"
                data=serializer.errors
                context['data']=data
                return Response(context)
        else:
            context['status']=400
            context['sucess']=False
            context['message']="not  created"
            data=serializer.errors
            context['data']=data
            return Response(context)
        
    def get(self, request, *args, **kwargs):
        if request.user.Is_University == 1:
            context={}
            data={}
            try:
                obj=get_object_or_404(Profile,User=request.user)
            except:
                context['sucess']=False
                context['status']=400
                context['message']="fill the form"
                context['data']=data
                return Response(context)
            
            serializer = UniversitySerializer(obj)
            context['sucess']=True
            context['status']=200
            context['message']="already exist"
            data=serializer.data
            context['data']=data
            return Response(context)
            
    def put(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.Is_University == 1:
            obj=get_object_or_404(Profile,User=request.user)
            serializer = UniversitySerializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
                
            

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def applyforjobUniversity(request,id):
    if request.method=="POST":
        context={}
        data={}
        obj=Jobs.objects.get(pk=id)
        U=request.user
        Profil=get_object_or_404(Profile,User=request.user )
        serializer=JobenquirySerializer(data=request.data)
        if serializer.is_valid():
            obj=serializer.save(University=Profil,job=obj)
            context['status']=200
            context['sucess']=True
            data=serializer.data
            context['message']="Sucessfully applied"
            context['data']=data
            return Response(context)
        else:
            context['status']=400
            context['sucess']=False
            data=serializer.errors
            context['message']="can't apply "
            context['data']=data
            return Response(context)



