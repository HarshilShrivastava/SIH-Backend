from django.shortcuts import render
from rest_framework.permissions import AllowAny
import requests
from Candidate.models import (
    Recruit,
    Skill,
    JobenquiryC,
    FulllistMarks,
    SocialMediaTags,
    SocioeconomicTags,
    Certificate,
    Skills

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
from rest_framework.parsers import (
    MultiPartParser, 
    FormParser)
from rest_framework.permissions import IsAuthenticated
from Candidate.serializers import( 
    RecruitSerializer,
    JobapplySerializer,
    ViewAppilicationSerializer,
    RatingMarketSerializer,
    RatingTechSerializer,
    GeneralMarkSerializer,
    subDomainMarkSerializer,
    FulllistMarksSerializer,
    DomainMarkSerializer,
    RecruitReadSerializer,
    CertificateSerializer
    )
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
                time=serializer.validated_data['Time']
                familyincome=int(serializer.validated_data['Familyincome'])
                residence=serializer.validated_data['Residence']
                residence=int(residence.id)
#for temporary condition of social media 
                time=int(time)
                if time>=4:
                    # extreme high
                    obj=SocialMediaTags.objects.get(pk=4)
                if time<=2:
                    #extreme low
                    obj=SocialMediaTags.objects.get(pk=5)
                if time<4 and time>2:
                        #moderate
                    obj=SocialMediaTags.objects.get(pk=6)
## socio economic condition
                if familyincome <=2:
                    if residence=='4' or residence ==4:
                        soectag=SocioeconomicTags.objects.get(pk=3)#T1

                    if residence=='3' or residence ==3:
                        soectag=SocioeconomicTags.objects.get(pk=4)#2
                    
                    if residence=='2' or residence ==2:
                        soectag=SocioeconomicTags.objects.get(pk=5)#T3
                    
                    if residence=='1' or residence ==1:
                        soectag=SocioeconomicTags.objects.get(pk=6)#T4

                if familyincome >2 and familyincome <4:
                    if residence=='4' or residence ==4:
                        soectag=SocioeconomicTags.objects.get(pk=7)#T5

                    if residence=='3' or residence ==3:
                        soectag=SocioeconomicTags.objects.get(pk=8)#T6
                    
                    if residence=='2' or residence ==2:
                        soectag=SocioeconomicTags.objects.get(pk=9)#T7
                    
                    if residence=='1' or residence ==1:
                        soectag=SocioeconomicTags.objects.get(pk=10)#T8

                if  familyincome >=4:
                    if residence=='4' or residence ==4:
                        soectag=SocioeconomicTags.objects.get(pk=11)#T9

                    if residence=='3' or residence ==3:
                        soectag=SocioeconomicTags.objects.get(pk=12)#T10
                    
                    if residence=='2' or residence ==2:
                        soectag=SocioeconomicTags.objects.get(pk=13)#T11
                
                    if residence=='1' or residence ==1:
                        soectag=SocioeconomicTags.objects.get(pk=14)#T12
                profile=serializer.save(User=self.request.user)
                profile.SocialMediaTags.add(obj)
                profile.SocioeconomicTags.add(soectag)
                url="http://sihml.pythonanywhere.com/analysis/analysis-get/"
                params = {'username': request.user}
                response = requests.post(url, data=params)
                for i in response.json():
                    obj,c=Skills.objects.get_or_create(Name=i)
                    profile.Skills.add(obj)


                profile.save()
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
            serializer = RecruitReadSerializer(obj)
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
                obj1=get_object_or_404(Recruit,User=request.user)
                marks=obj1.MarketRating
                marks1=obj1.TechRating
                time=obj1.Time
                mark=max(marks,marks1)
                if mark>=3.5:
                    if time>=4:
                    # extreme high
                        objx=SocialMediaTags.objects.get(pk=7)
                    if time<=2:
                        #extreme low
                        objx=SocialMediaTags.objects.get(pk=8)
                    if time<4 and time>2:
                            #moderate
                        objx=SocialMediaTags.objects.get(pk=9)
                elif mark <3.5 and mark >2.0:
                    if time>=4:
                    # extreme high
                        objx=SocialMediaTags.objects.get(pk=10)
                    if time<2:
                        #extreme low
                        objx=SocialMediaTags.objects.get(pk=11)
                    if time<4 and time>2:
                            #moderate
                        objx=SocialMediaTags.objects.get(pk=12)        
                else:
                    if time>=4:
                    # extreme high
                        objx=SocialMediaTags.objects.get(pk=13)
                    if time<=2:
                        #extreme low
                        objx=SocialMediaTags.objects.get(pk=14)
                    if time<4 and time>2:
                            #moderate
                        objx=SocialMediaTags.objects.get(pk=15)
                obj1.SocialMediaTags.add(objx)     
                obj1.save()             

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
def put_ratingM(request):
    context={}
    data={}
    if request.user.Is_Candidate==0:
        context['status']=400
        context['sucess']=False
        context['message']="Unauthorised acess "
        context['data']=data
        return Response(context)
    serializer=RatingMarketSerializer(data=request.data)
    if serializer.is_valid():
        obj=get_object_or_404(Recruit,User=request.user)
        X=serializer.data['MarketRating']
        prev=obj.MarketRating
        no=obj.AttemptMarket
        #new_val=(no*prev+X)/no+1
        new_val=no*prev
        new_val=int(new_val)+int(X)
        no=no+1
        new_val=new_val/no
        obj.MarketRating=new_val
        obj.AttemptMarket=no
        obj.save()
        obj1=get_object_or_404(Recruit,User=request.user)
        marks=obj1.MarketRating
        marks1=obj1.TechRating
        time=obj1.Time
        mark=max(marks,marks1)
        if mark>=3.5:
            print("hello world")
            if time>=4:
            # extreme high
                obj=SocialMediaTags.objects.get(pk=7)
            if time<=2:
                #extreme low
                obj=SocialMediaTags.objects.get(pk=8)
            if time<4 and time>2:
                obj=SocialMediaTags.objects.get(pk=9)
        elif mark <3.5 and mark >2.0:
            if time>=4:
            # extreme high
                obj=SocialMediaTags.objects.get(pk=10)
            if time<=2:
                #extreme low
                obj=SocialMediaTags.objects.get(pk=11)
            if time<4 and time>2:
                    #moderate
                obj=SocialMediaTags.objects.get(pk=12)        
        else:
            if time>=4:
            # extreme high
                obj=SocialMediaTags.objects.get(pk=13)
            if time<=2:
                #extreme low
                obj=SocialMediaTags.objects.get(pk=14)
            if time<4 and time>2:
                    #moderate
                obj=SocialMediaTags.objects.get(pk=15)
        obj1.SocialMediaTags.add(obj)     
        obj1.save()             
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

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def put_ratingT(request):
    context={}
    data={}
    if request.user.Is_Candidate==0:
        context['status']=400
        context['sucess']=False
        context['message']="Unauthorised acess "
        context['data']=data
        return Response(context)
    serializer=RatingTechSerializer(data=request.data)
    if serializer.is_valid():
        obj=get_object_or_404(Recruit,User=request.user)
        X=serializer.data['TechRating']
        prev=obj.TechRating
        no=obj.AttemptTech
        #new_val=(no*prev+X)/no+1
        new_val=no*prev
        new_val=new_val+X
        no=no+1
        new_val=new_val/no
        obj.TechRating=new_val
        obj.AttemptTech=no
        obj.save()
        obj1=get_object_or_404(Recruit,User=request.user)
        marks=obj1.MarketRating
        marks1=obj1.TechRating
        time=obj1.Time
        mark=max(marks,marks1)
        if mark>=3.5:
            print("hello world")
            if time>=4:
            # extreme high
                obj=SocialMediaTags.objects.get(pk=7)
            if time<=2:
                #extreme low
                obj=SocialMediaTags.objects.get(pk=8)
            if time<4 and time>2:
                obj=SocialMediaTags.objects.get(pk=9)
        elif mark <3.5 and mark >2.0:
            if time>=4:
            # extreme high
                obj=SocialMediaTags.objects.get(pk=10)
            if time<=2:
                #extreme low
                obj=SocialMediaTags.objects.get(pk=11)
            if time<4 and time>2:
                    #moderate
                obj=SocialMediaTags.objects.get(pk=12)        
        else:
            if time>=4:
            # extreme high
                obj=SocialMediaTags.objects.get(pk=13)
            if time<=2:
                #extreme low
                obj=SocialMediaTags.objects.get(pk=14)
            if time<4 and time>2:
                    #moderate
                obj=SocialMediaTags.objects.get(pk=15)
        obj1.SocialMediaTags.add(obj)     
        obj1.save()             
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

@api_view(['POST', ])
@permission_classes((AllowAny, ))
def put_generalmarks(request):
    context={}
    data={}

    serializer=GeneralMarkSerializer(data=request.data)
    if serializer.is_valid():
        obj=serializer.save()
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

@api_view(['POST', ])
@permission_classes((AllowAny, ))
def put_domainmarks(request):
    context={}
    data={}
    if request.user.Is_Candidate==0:
        context['status']=400
        context['sucess']=False
        context['message']="Unauthorised acess "
        context['data']=data
        return Response(context)
    serializer=DomainMarkSerializer(data=request.data)
    if serializer.is_valid():
        obj=serializer.save()
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


# subDomainMarkSerializer
@api_view(['POST', ])
@permission_classes((AllowAny, ))
def put_sub_domainmarks(request):
    context={}
    data={}

    serializer=subDomainMarkSerializer(data=request.data)
    if serializer.is_valid():
        obj=serializer.save()
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

class Fullmarks(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    def post(self, request, *args, **kwargs):
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
            serializer = FulllistMarksSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(Recruit=obj)
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
            qs=FulllistMarks.objects.filter(Recruit=obj)
            serializer = FulllistMarksSerializer(qs,many=True)
            context['sucess']=True
            context['status']=200
            context['count']=qs.count()
            data=serializer.data
            context['data']=data
            return Response(context)

class CertificateView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    def post(self, request, *args, **kwargs):
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
            serializer=CertificateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(Recruit=obj)
                context['sucess']=True
                context['status']=200
                context['response']="sucessfull post"
                return Response(context)
            else:
                context['sucess']=False
                context['status']=400
                context['response']="unsucessfull post"
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
            qs=Certificate.objects.filter(Recruit=obj)
            serializer=CertificateSerializer(qs,many=True)
            context['sucess']=True
            context['status']=200
            context['response']="sucessfull post"
            context['count']=qs.count()
            context['data']=serializer.data
            return Response(context)
