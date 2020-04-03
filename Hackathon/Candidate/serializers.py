from .models import Recruit,MCQresult,Skill,JobenquiryC
from rest_framework import serializers
class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recruit
        fields=["Name","Address","Resume"]
class JobapplySerializer(serializers.ModelSerializer):
    class Meta:
        model=JobenquiryC
        fields=['proposal']