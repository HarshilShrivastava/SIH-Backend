
from rest_framework import serializers
from customquiz.models import Question,Answer

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=['key','Question_text','Domain']

class AnswerSerializer(serializers.ModelSerializer):
    Question_related_to=serializers.IntegerField()

    class Meta:
        model=Answer
        fields=['Answer_text','Weightage','Question_related_to']