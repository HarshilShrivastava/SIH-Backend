from quiz.models import(
     Answer,
     DomainQuestion,
     Question,
     SubDomain
)
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view,permission_classes
from quiz.api.serializers import (
QuestionSerializer,
AnswerSerializer,
DomainQuestionSerializer,



)
from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.response import Response

class QuestiontListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)


    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'Question_list': serializer.data})

class DomainQuestiontListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = DomainQuestion.objects.all()
    serializer_class = DomainQuestionSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Domain']

    def list(self, request, *args, **kwargs):
        context={}
        data={}
        context['sucess']=True
        context['status']=200
        context['response']="sucessfull"
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        data=serializer.data
        context['data']=data
        return Response(context)



@api_view( ['GET'])
@permission_classes((AllowAny,))
def Level3qa(request,id1,id2):
    context={}
    data={}
    d1=get_object_or_404(SubDomain,pk=id1)
    qs1=DomainQuestion.objects.filter(SubDomain=d1)
    d2=get_object_or_404(SubDomain,pk=id2)
    qs1=qs1 | DomainQuestion.objects.filter(SubDomain=d2)
    context['sucess']=True
    context['status']=200
    context['message']='sucessfull get'
    context['count']=qs1.count()
    serializer=DomainQuestionSerializer(qs1,many=True)
    data=serializer.data
    context['data']=data
    return Response(context)
