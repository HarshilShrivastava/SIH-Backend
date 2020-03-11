from .models import Recruit,MCQresult,Skill
from rest_framework import serializers
class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recruit
        fields=["Name","Address","Resume"]
