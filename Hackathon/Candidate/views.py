from django.shortcuts import render
from Candidate.models import (
    Recruit,
    Skill,
    MCQresult,
    JobenquiryC,

    )
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from Organization.models import(
    Jobs
)
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import RecruitSerializer,JobapplySerializer,ViewAppilicationSerializer,RatinfSerializer
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
            
      

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def applyforjob(request,id):
    if request.method=="POST":
        context={}
        data={}
        obj=Jobs.objects.get(pk=id)
        U=request.user
        Profil=get_object_or_404(Recruit,User=request.user )
        serializer=JobapplySerializer(data=request.data)
        if serializer.is_valid():
            obj=serializer.save(Recruit=Profil,job=obj)
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



@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def list_of_job(request):
    context={}
    data={}
    if request.user.Is_Candidate==0:
        context['status']=400
        context['sucess']=False
        context['message']="Unauthorised acess "
        context['data']=data
        return Response(context)
    obj=get_object_or_404(Recruit,User=request.user)
    qs=JobenquiryC.objects.filter(Recruit=obj)
    serializer=ViewAppilicationSerializer(qs,many=True)
    context['status']=200
    context['sucess']=True
    data=serializer.data
    context['message']="Sucessfull get"
    context['count']=qs.count()
    context['data']=data
    return Response(context)
    

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def put_rating(request):
    context={}
    data={}
    if request.user.Is_Candidate==0:
        context['status']=400
        context['sucess']=False
        context['message']="Unauthorised acess "
        context['data']=data
        return Response(context)
    serializer=RatinfSerializer(data=request.data)
    if serializer.is_valid():
        obj=get_object_or_404(Recruit,User=request.user)
        X=serializer.data['Rating']
        prev=obj.Rating
        no=obj.No_of
        #new_val=(no*prev+X)/no+1
        new_val=no*prev
        new_val=new_val+X
        no=no+1
        new_val=new_val/no
        obj.Rating=new_val
        obj.No_of=no
        obj.save()
        context['status']=200
        context['sucess']=True
        context['message']="Sucessfull applied marks"
        context['data']=data
        return Response(context)
    else:
        context['status']=204
        context['sucess']=False
        context['message']="didn't update marks "
        context['data']=data
        return Response(context)

