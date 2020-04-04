from quiz.models import(
     Answer,
     DomainQuestion,
     Question
)
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view,permission_classes
from quiz.api.serializers import (
QuestionSerializer,
AnswerSerializer,
DomainQuestionSerializer,
DomainMarksSerializer,
GeneralMarksSerializer

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


@api_view( ['POST'])
@permission_classes((AllowAny,))
def putgeneralmarks(request):
    if request.method=="POST":
        serializer=GeneralMarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view( ['POST'])
@permission_classes((AllowAny,))
def putdomainmarks(request):
    if request.method=="POST":
        serializer=DomainMarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


