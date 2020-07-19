from django.shortcuts import render
from .models import Company,Jobs,SkillForJobs
from rest_framework import filters
from Candidate.models import(
    JobenquiryC
)
import requests
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny

from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import companyserializer,jobserializer,jobReadserializer,ResultSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from Candidate.models import (
    Recruit
)
from Candidate.serializers import(
    ApplicationSerializer
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
                context['status']=404
                context['message']="profile not created"
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
            profile=serializer.save(by=companyobj)
            print(profile)
            context['sucess']=True
            context['response']="sucessfull"
            text=serializer.validated_data['Job_Descreption']
            url="http://sihml.pythonanywhere.com/analysis/skills-get/"
            params = {'Txt': text}
            response = requests.post(url, data=params)
            print(response.json())
            x=Jobs.objects.get(id =profile.id)
            print(x)
            for i in response.json():
                obj,c=SkillForJobs.objects.get_or_create(Name=i)
                print(obj)
                x.SkillRequired.add(obj)
            x.save()
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


@api_view(['POST', ])
@permission_classes((AllowAny, ))   
def Recommendedjobs(request):
    if request.method=='POST':
        serializer=ResultSerializer(data=request.data)
        if serializer.is_valid():
            first=serializer.data['first']
            Second=serializer.data['Second']
            third=serializer.data['third']
            fourth=serializer.data['fourth']
            jobsqs=Jobs.objects.filter(SubDomain=first).filter(SubDomain=Second).filter(SubDomain=third).filter(SubDomain=fourth)
            jobsqscount=jobsqs.count()
            first_ratio=0.4*jobsqscount
            Second_ratio=0.3*jobsqscount
            third_ratio=0.2*jobsqscount
            fourth_ratio=0.1*jobsqscount
            final=Jobs.objects.none().distinct()
            final=final|Jobs.objects.filter(SubDomain=first)[:first_ratio]
            final=final|Jobs.objects.filter(SubDomain=first)[:Second_ratio]
            final=final|Jobs.objects.filter(SubDomain=first)[:third_ratio]
            final=final|Jobs.objects.filter(SubDomain=first)[:fourth_ratio]
            finalqs=jobReadserializer(final,many=True)
            data={}
            context={}
            context['sucess']=True
            context['status']=200
            context['count']=jobsqscount
            context['message']="sucessfull get"
            data=finalqs.data
            context['data']=data
            return Response (context)
        else:
            context['sucess']=False
            context['status']=401
            context['message']=serializer.errors
            context['data']=data
            return Response (context)



class AllJobViews(generics.ListCreateAPIView):
    queryset=Jobs.objects.all()
    serializer_class = jobReadserializer
    search_fields = ['^job_title','by__Name']
    filter_backends = (filters.SearchFilter,)
    def list(self,request,*args,**kwargs):
        self.object_list=self.filter_queryset(self.get_queryset())
        serializer=self.get_serializer(self.object_list,many=True)
        context={}
        data={}
        context['sucess']=True
        context['status']=200
        context['response']="sucessfull"
        context['count']=self.object_list.count()
        data=serializer.data
        context['data']=data
        return Response(context)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))    
def list_of_application(request,id):
    context={}
    data={}
    if request.user.Is_Organization==0:
        context['sucess']=False
        context['status']=400
        context['message']="unsucessfull get"
        context['data']=data
        return Response(context)
    
    obj=get_object_or_404(Jobs,pk=id)
    if request.user == obj.by.User:
        qs=JobenquiryC.objects.filter(job=obj).order_by("-similarity")
        context['sucess']=True
        context['status']=200
        context['message']="sucessfull get"
        context['count']=qs.count()
        serializer=ApplicationSerializer(qs,many=True)
        data=serializer.data
        context['data']=data
        return Response(context)
    else:
        context['sucess']=False
        context['status']=400
        context['message']=" unauthorised acess"
        context['data']=data
        return Response(context)

