from django.shortcuts import render
from rest_framework.permissions import AllowAny
from content.models import(
    Blogs,
    Courses,
    Scheme
)
from rest_framework import filters

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
from rest_framework import generics

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def RecommendedCourses(request):
    obj=get_object_or_404(Recruit,User=request.user)
    qs=Courses.objects.none().distinct()
    smt=obj.SocioeconomicTags.all()
    for i in smt:
        qs=qs | Courses.objects.filter(SocioeconomicTags=i.id)
    
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
    print(obj)
    qs=Blogs.objects.none().distinct()
    smt=obj.SocialMediaTags.all()
    print(smt)
    for i in smt:
        print(i.id)
        qs=qs | Blogs.objects.filter(SocialMediaTags=i)
        print(qs)

    context={}
    data={}
    print
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
        qs=qs | Scheme.objects.filter(SocioeconomicTags=i)
    context={}
    data={}
    serializer=SchemeSerializers(qs,many=True)
    data=serializer.data

    context['status']=200
    context['message']="sucessfull get"
    context['count']=qs.count()
    context['data']=data
    return Response(context)



class AllBlogsViews(generics.ListCreateAPIView):
    queryset=Blogs.objects.all()
    serializer_class = BlogsSerializers
    search_fields = ['^Title','^Description']
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
        
class AllSchemeViews(generics.ListCreateAPIView):
    queryset=Scheme.objects.all()
    serializer_class = SchemeSerializers
    search_fields = ['^Title','^Description','^By']
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
        
    
class CoursesViews(generics.ListCreateAPIView):
    queryset=Courses.objects.all()
    serializer_class = CourseSerializers
    search_fields = ['^Title','^Description','^By']
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