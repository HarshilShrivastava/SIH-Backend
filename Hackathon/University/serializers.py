from rest_framework import serializers
from .models import Profile,Jobenquiry
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["Name","Address","Website","Conteact_no","Type","University","AICTE_college_code","Email"]

class JobenquirySerializer(serializers.ModelSerializer):
    class Meta:
        model=Jobenquiry
        fields=['proposal']