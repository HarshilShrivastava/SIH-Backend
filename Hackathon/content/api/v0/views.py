from django.shortcuts import render
from rest_framework.permissions import AllowAny
from content.models import(
    Blogs,
    Courses,
    Scheme
)
from Candidate.models import Recruit
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication

from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from content.api.v0.serializers import( 
    BlogsSerializers,
    CourseSerializers,
    SchemeSerializers
    )
from rest_framework.views import APIView

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def RecommendedCourses(request):
    obj=get_object_or_404(Recruit,User=request.user)
    qs=Courses.objects.none().distinct()
    smt=obj.SocioeconomicTags.all()
    for i in smt:
        qs=Courses.objects.filter(SocioeconomicTags=i)
    

    #lis=Courses.objects.all().None()

    context={}
    data={}
    serializer=CourseSerializers(qs,many=True)
    data=serializer.data
    context['status']=200
    context['message']="sucessfull get"
    context['count']=qs.count()
    context['data']=data
    return Response(context)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def RecommendedBlogs(request):
    obj=get_object_or_404(Recruit,User=request.user)
    qs=Blogs.objects.none().distinct()
    smt=obj.SocialMediaTags.all()
    for i in smt:
        qs=Blogs.objects.filter(SocialMediaTags=i)

    context={}
    data={}
    serializer=BlogsSerializers(qs,many=True)
    context={}
    data={}
    data=serializer.data
    context['status']=200
    context['message']="sucessfull get"
    context['count']=qs.count()
    context['data']=data
    return Response(context)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def RecommendedScheme(request):
    obj=get_object_or_404(Recruit,User=request.user)
    qs=Scheme.objects.none().distinct()
    smt=obj.SocioeconomicTags.all()
    for i in smt:
        qs=Scheme.objects.filter(SocioeconomicTags=i)
    context={}
    data={}
    serializer=SchemeSerializers(qs,many=True)
    data=serializer.data

    context['status']=200
    context['message']="sucessfull get"
    context['count']=qs.count()
    context['data']=data
    return Response(context)